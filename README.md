# Build@Mercari Training Program 2022

This is Team10's build training repository.


## Tasks

- [x] **STEP1** Git ([JA](document/step1.ja.md)/[EN](document/step1.en.md))
- [x] **STEP2** Setup environment ([JA](document/step2.ja.md)
  /[EN](document/step2.en.md))
- [x] **STEP3** Develop API ([JA](document/step3.ja.md)
  /[EN](document/step3.en.md))
- [x] **STEP4** Docker ([JA](document/step4.ja.md)/[EN](document/step4.en.md))
- [ ] **STEP5** (Stretch) Frontend ([JA](document/step5.ja.md)
  /[EN](document/step5.en.md))
- [x] **STEP6** (Stretch)  Run on docker-compose ([JA](document/step6.ja.md)
  /[EN](document/step6.en.md))

### Other documents

- 効率的に開発できるようになるためのTips / Tips for efficient development ([JA](document/tips.ja.md)/[EN](document/tips.en.md))
	
--- 
# AI Checker

# Hackweek 5/23-5/31
  
- Kickoff meeting note [ドキュメント(閲覧制限あり)](https://docs.google.com/document/d/12-YTNs6I2TAsNm49sLjNW2BjZ1_bQp2jSE6_KqkZD_Y/edit?userstoinvite=tkat0@mercari.com#)
  
## 注意⚠️
  
- 現在step5にあたる、POSTに対しての画像ファイル処理にエラーが発生しているため、ItemList.tsc内ではPlaceholderファイルを表示している
  	
- ブランチstep5はこのエラー解消用
	
## DEMO VIDEO
	[Youtube](https://youtu.be/Gzsw_WLsBCM)
  
## ブランチ運用


	  main—------(念の為おいておく)
				|- HackWeek (デモ用)
					|- frontend(typescript用) :森本さん
					|- Backend:大村さん　(以前の評価関数)
					|- Unit Tests
					|- newDB (最新)
					|- checker (以前のDB)
						|_newOpenCV(新しい評価関数)
	
	
	
## アプリの動かし方
	
1. 一つ目のターミナルでサーバーでアプリを実行
	
	```
	cd python
	uvicorn main:app --reload --port 9000
	```
	
2. 二つ目のターミナルでフロントエンドを動かす
	
	```
	cd typescript/simple-mercari-web
	```
	
	* ↓一回目だけ　参照([JA](document/step5.ja.md))
	
	```
	npm ci 
	```
	
	* 実行
	```
	npm start
	```
	
	ブラウザからhttp://localhost:3000/にアクセス
	

	* 下が表示されたら成功(23日時点)
	
	<img width="1334" alt="Screen Shot 0004-05-23 at 17 00 44" src="https://user-images.githubusercontent.com/30760730/169860383-c2940bc9-a7b1-4fc2-8354-8ab2048249ba.png">

	
## TODO
  - Frontend : [フロントエンド](hackweek-document/frontend.md)
  - Backend :　[バックエンド](hackweek-document/backend.md)
  - Error : [エラー](hackweek-document/error.md)
  

  
