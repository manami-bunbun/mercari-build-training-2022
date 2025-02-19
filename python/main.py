import collections
import os
import logging
import pathlib
import shutil
from fastapi import FastAPI, Form, HTTPException
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import random
import sqlite3
import json
from fastapi.responses import ORJSONResponse
import hashlib
from openCV import condition 



#----config----------------------------

app = FastAPI()
logger = logging.getLogger("uvicorn")
logger.level = logging.INFO
images = pathlib.Path(__file__).parent.resolve() / "images"
image = pathlib.Path(__file__).parent.resolve() / "image"
origins = [ os.environ.get('FRONT_URL', 'http://localhost:3000') ]
url = 'http://localhost:9000'
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET","POST","PUT","DELETE"],
    allow_headers=["*"],
)

# ----methods----------------------------

def db_toList(items):
    objects_list = []
    for row in items:
        d = collections.OrderedDict()
        d['id'] = row[0]
        d['name'] = row[1]
        d['category'] = row[2]
        d['image_filename'] = row[3]
        d['score'] = row[4]
        # d['checked_imagename'] = row[5]
        objects_list.append(d)   
    return objects_list 

def image_toHash(image_filename):
    image_name, image_fmt = map(str, image_filename.split('.'))
    image_hashname = hashlib.sha256(image_name.encode()).hexdigest()
    return '.'.join([image_hashname, image_fmt])

def save_image(file_location, image_file):
    with open(file_location, 'w+b') as f:
        shutil.copyfileobj(image_file.file, f) 
        
def add_sql(name,category, image_name, score, checked_imagename):
    conn = sqlite3.connect("../db/item.db", check_same_thread=False)
    c = conn.cursor()
    c.execute("INSERT INTO items(name,category,image_filename, score, checked_imagename) VALUES( ?, ?, ?, ?, ?);", (name,category,image_name , score, checked_imagename))
    # idはtable作成時に割り当て済み
    conn.commit()
    conn.close()
 
    
# ----endpoints--------------------------

@app.get("/")
def root():
    return {"message": "Hello, world!"}

# curl -X GET 'http://127.0.0.1:9000/items'
@app.get("/items", response_class=ORJSONResponse)
def show_item():
    conn = sqlite3.connect("../db/item.db", check_same_thread=False)
    c = conn.cursor()
    items = c.execute('SELECT id, name,category,image_filename, score FROM items;').fetchall()
    content = db_toList(items)
    conn.close()
    return {"items": content}

# curl -X POST \
#   --url 'http://localhost:9000/items' \
#   -d 'name=jacket' \
#   -d 'category=fashion' \
#   -d 'image=images/default.jpg' \
#   -d ''
@app.post("/items")
def add_item(name: str = Form(...), category: str = Form(...), image: UploadFile = File(...)):
    
    #imageNameハッシュ化
    image_hashname = image_toHash(image.filename) 
    file_location = f"image/{image_hashname}"
    save_image(file_location,image)
    logger.info(f"Receive item: {image_hashname}") 
    
    #OpenCV.py
    score, checked_imagename = condition(file_location)
    logger.info(f"score: {score}")
    
    #DB
    add_sql(name,category,image_hashname, score, checked_imagename)

    return {"message": f"item received: {name}"}


# curl -X GET 'http://127.0.0.1:9000/search?keyword=jacket'
@app.get("/search" , response_class=ORJSONResponse)
def search_item(keyword: str = None):
    conn = sqlite3.connect('../db/item.db')
    c = conn.cursor()
    items = c.execute('SELECT name,category,image_filename FROM items WHERE name LIKE  ? ;', (f"%{keyword}%",)).fetchall()
    content = db_toList(items)
    conn.close()
    return {"items": content}



# curl -X GET 'http://127.0.0.1:9000/items/(id)'
# {"items":[{"id":1,"name":"jacket","category":"fashion","image":"ad55d25f2c10c56522147b214aeed7ad13319808d7ce999787ac8c239b24f71d.jpg"}]}
@app.get("/items/{item_id}", response_class=ORJSONResponse)
def show_detailById(item_id: int):
    logger.info(f"Search item: {item_id}")
    conn = sqlite3.connect('../db/item.db')
    c = conn.cursor()
    items = c.execute("SELECT * from items WHERE id=(?)", (item_id,)).fetchone()
    content = db_toList(items)
    conn.close()
    return {"items": content}



@app.get("/image/{image_filename}")
def get_image(image_filename):
    # Create image path
    logger.info(f"image_file:{image_filename}")

    image_path =  image / image_filename
    #..../mercari/mercari-build-training-2022/python/image/undefinedが返ってくる
    logger.info(f"image_location::{image_path}")
    
    if not image_filename.endswith(".jpg"):
        raise HTTPException(status_code=400, detail="Image path does not end with .jpg")
    

    if not image_path:
        logger.debug(f"Image not found: {image_filename}")
        image_path = images / "default.jpg"
    
        
    return FileResponse(image_path)


@app.get("/check/{id}")
def get_checked(id):
    conn = sqlite3.connect('../db/item.db')
    c = conn.cursor()
    score = c.execute('SELECT score FROM items WHERE id =  ? ;', (id),).fetchone() 
    conn.close()
    return score
