from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return "Hello World"

# mysql_api/db_api.py

# Các import cần thiết (Flask, SQLAlchemy, vv...)
from flask import jsonify
from .models import db, Product  # Giả định bạn đã định nghĩa model và db

def get_products_from_db():
    products = Product.query.all()
    products_list = [{
        'imageUrl': product.image_url,
        'phoneModel': product.model,
        'ram': product.ram,
        'storage': product.storage,
        'price': product.price,
        'location': product.location
    } for product in products]
    return products_list
