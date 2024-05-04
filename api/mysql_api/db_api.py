from flask import Flask
import requests
import mysql.connector as conn

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello to db_api!"


def connect_to_db():
    db_config = { 
        'host': 'mysql_service',
        'port': '3306',
        'user': 'root',
        'password': 'psw123',
        'database': 'local_db'
    }
    return conn.connect(**db_config)

def get_products_from_crawling():
    # products = get_products()
    url = 'http://localhost:5000/get_products'
    products = requests.get(url).json()
    return products

@app.route('/test_connection')
def test_connection():
    try:
        connection = connect_to_db()
        connection.close()
        return "OK"
    except conn.Error as e:
        return {"error": str(e)}

@app.route('/delete')
def delete_products():
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM products")
        connection.commit()
        cursor.close()
        connection.close()
        return "OK"
    except conn.Error as e:
        return {"error": str(e)}

@app.route('/fetch')    
def fetch():
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM products")
        connection.commit()
        stmt = "INSERT INTO products (product_id, name, price, quantity, image) VALUES"
        for product in get_products_from_crawling():
            stmt += f"\n({product['product_id']}, '{product['name']}', {product['price']}, {product['quantity']}, '{product['image']}'),"
        cursor.execute(stmt[:-1])
        connection.commit()
        cursor.close()
        connection.close()
        return "OK"
    except conn.Error as e:
        return {"error": str(e)}
    
@app.route('/list')
def list_products():
    return get_products_from_crawling()
    
@app.route('/products')
def list_products_json_form():
    fetch()
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products")
        products = [{'product_id': product[0],
                     'name': product[1],
                     'price': product[2],
                     'quantity': product[3],
                     'image': product[4]} for product in cursor.fetchall()]
        cursor.close()
        connection.close()
        return products
    except conn.Error as e:
        print(e)
        return {"error": str(e)}
        
def test():
    url = 'http://localhost:5000/get_products'

    # Gửi yêu cầu GET đến API
    response = requests.get(url)

    # Kiểm tra mã trạng thái HTTP để đảm bảo yêu cầu thành công
    if response.status_code == 200:
        # Xử lý dữ liệu trả về
        data = response.json()
        print(data)
    else:
        print(f'Failed to retrieve data: {response.status_code}')
    
    
def main(host='0.0.0.0', port=5001):
    app.run(debug=True, host=host, port=port)
    
if __name__ == "__main__":
    # test()
    main()
    