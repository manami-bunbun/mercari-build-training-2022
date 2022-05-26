import sqlite3
from fastapi.testclient import TestClient
import os

from main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}


# TODO: responceの中を埋める(item.db使用)
def test_read_item():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == {
        "name": "",
        "category": "",
        "image": "",
    }

# TODO: responceの中を埋める(item.db使用)
def test_create_item():
    response = client.post(
        "/items",  
        json={"name":"jacket", "category":"fashion", "image":"images/defalut.jpg"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "",
        "category": "",
        "image": "",
    }
