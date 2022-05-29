import cv2
import numpy as np



def condition(img_path):
    
   #パスの設定
    origin_path = img_path
    obj_path = 'checked_image/obj.jpg'
    mask_path = 'checked_image/mask.jpg'
    result_path = 'checked_image/result.jpg'
    
    # 元画像を読み込む
    img = cv2.imread(origin_path,0)
    
    #---------前処理----------------------
    
    #Canny法
    edges4 = cv2.Canny(img,50,800)
    cv2.imwrite(obj_path, edges4)
    
    # スマートフォンの外部を真っ黒にするフィルターを作る
    ret,img_bin = cv2.threshold(img,20,400,cv2.THRESH_BINARY)
    img_bin = cv2.bitwise_not(img_bin) # 白黒反転

    # カーネルを作成
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

    # 収縮
    img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel, iterations=10)

    #スマホの形を浮き出さセルマスクを作成
    cv2.imwrite(mask_path, img_bin)
    
    #マスクとCanny法で出したエッジで、傷を白く浮き出させる
    img_obj = cv2.imread(obj_path, 0)
    img_mask = cv2.imread(mask_path, 0)

    img_mask_inv = cv2.bitwise_not(img_mask)
    img_edge = cv2.bitwise_and(img_obj, img_mask_inv)
    img_obj = cv2.bitwise_xor(img_obj, img_edge)
    cv2.imwrite(obj_path, img_obj)
    
    # -----スコア----------------------
    
    img_gray = cv2.imread(obj_path, 0)
    img_mask = cv2.imread(mask_path, 0) 
    
    #スマートフォンの画素数（マスクの画像の白い部分）
    white_area=cv2.countNonZero(img_mask)
    #傷の画素数
    kizu=cv2.countNonZero(img_gray)
    #スコア
    score = round(kizu/white_area*100,1)
    
    if score < 0:
        score =0
    
    #---------ラベリング(未使用)---------------

    # ラベリング処理
    n, label, data, center = cv2.connectedComponentsWithStats(img_gray)
    sizes = data[1:, -1]
    
    # ラベリング結果書き出し準備
    img_result = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    
    # サイズフィルター
    for i in range(1, n):
        if sizes[i-1]< white_area/1.5:
            #img_result[label==i] = 255
            # 各オブジェクトの外接矩形を赤枠で表示
            x0 = data[i][0]-2
            y0 = data[i][1]-2
            x1 = x0 + data[i][2] +4
            y1 = y0 + data[i][3] +4
            cv2.rectangle(img_result, (x0, y0), (x1, y1), color=(0, 0, 255), thickness=3)

    # 結果画像を書き出し
    cv2.imwrite(result_path , img_result)

    
    return score, result_path
