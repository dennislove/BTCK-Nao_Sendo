from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello to Data_crawling!"

def crawling(url):
    response = requests.get(url)
    data = response.json()['data']
    return data

@app.route('/get_products')
def get_products():
    data1 = crawling("https://recommend-api.sendo.vn/web/listing/recommend/internal?track_id=06e0e029-b875-4764-8d54-e0ac6570928e&p=1&s=100&cate_path=thoi-trang-nu&sort_type=vasup_desc&platform=desktop2&app_verion=2.39.3&session_key=1714816781570&version=v2&is_new_listing=2")       
    data2 = crawling("https://recommend-api.sendo.vn/web/listing/recommend/internal?track_id=06e0e029-b875-4764-8d54-e0ac6570928e&p=2&s=100&cate_path=thoi-trang-nu&sort_type=vasup_desc&platform=desktop2&app_verion=2.39.3&session_key=1714816781570&version=v2&is_new_listing=2")
    data3 = crawling("https://recommend-api.sendo.vn/web/listing/recommend/internal?track_id=06e0e029-b875-4764-8d54-e0ac6570928e&p=3&s=100&cate_path=thoi-trang-nu&sort_type=vasup_desc&platform=desktop2&app_verion=2.39.3&session_key=1714816781570&version=v2&is_new_listing=2")
    data = data1+data2+data3
    seen_ids = set()
    products = []
    for product in data:
        product_id = product['item']['product_id']
        product_name = product['item']['name']
        
        # Kiểm tra tính hợp lệ của tên sản phẩm
        if product_id not in seen_ids and ('𝑭𝑹𝑬𝑬𝑺𝑯𝑰𝑷' not in product_name):
            products.append({
                'product_id': product_id,
                'name': product_name,
                'price': product['item']['price'],
                'quantity': product['item']['quantity'] if 'quantity' in product['item'] else 1,
                'image': product['item']['thumbnail_url']
            })
            seen_ids.add(product_id)
    return products

def test():
    print(get_products())
    
def main(host='0.0.0.0', port=5000):
    app.run(host=host, port=port)

if __name__ == "__main__":
#    test()
    main()