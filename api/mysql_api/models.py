# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(256), nullable=True)
    # Định nghĩa thêm các trường khác theo cơ sở dữ liệu của bạn

    def __repr__(self):
        return f'<Product {self.name}>'
