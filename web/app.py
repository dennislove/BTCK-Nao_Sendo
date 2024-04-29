# web_api/app.py

from flask import Flask, render_template, jsonify
from mysql_api.db_api import get_products_from_db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/api/products')
# def products():
#     products_data = get_products_from_db()
#     return jsonify(products_data)

if __name__ == '__main__':
    app.run(debug=True)
