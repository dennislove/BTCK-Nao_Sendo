from flask import Flask
import requests
import time
import threading
import logging

logging.basicConfig(filename='/data_crawling/log_file.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

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
    logging.info('chạy /get_products')
    logging.info('bắt đầu cào dữ liệu')
    data1 = crawling("https://recommend-api.sendo.vn/web/listing/recommend/internal?track_id=06e0e029-b875-4764-8d54-e0ac6570928e&p=1&s=100&cate_path=thoi-trang-nu&sort_type=vasup_desc&platform=desktop2&app_verion=2.39.3&session_key=1714816781570&version=v2&is_new_listing=2")       
    data2 = crawling("https://recommend-api.sendo.vn/web/listing/recommend/internal?track_id=144a92b2-3f9f-482e-b1a7-b12b478ac937&p=1&s=100&cate_path=quat&sort_type=vasup_desc&platform=desktop2&app_verion=2.39.3&session_key=1714839580730&version=v2&is_new_listing=2")
    data3 = crawling("https://recommend-api.sendo.vn/web/listing/recommend/internal?track_id=144a92b2-3f9f-482e-b1a7-b12b478ac937&p=1&s=100&cate_path=thiet-bi-cham-soc-quan-ao&sort_type=vasup_desc&platform=desktop2&app_verion=2.39.3&session_key=1714840565419&version=v2&is_new_listing=2")
    data = data1 + data2 + data3
    logging.debug(data)
    logging.info('đã cào dữ liệu')
    seen_ids = set()
    products = []
    for product in data:
        if 'is_empty' not in product:
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
    logging.info('đã format dữ liệu thành json')
    return products
    
def frequency_crawling():
    # products = get_products()
    url = 'http://db_api:5001/fetch'
    check = requests.get(url).json()
    logging.info(f'cập nhật dữ liệu: {check}')
    return check

def get_file_value(file_path):
    # Mở file và đọc hai dòng
    with open(file_path, "r") as file:
        data = file.read()
        value = int(data)
        logging.info(f'đọc file {file_path} dữ liệu: {value}')
        return value               

def run_schedule():
    file_path = '/data_crawling/config.txt'        
    while True:
        t = get_file_value(file_path)
        logging.info(f'bắt đầu cào và cập nhật dữ liệu {t} giây 1 lần')
        time.sleep(t)
        frequency_crawling()
        

@app.route("/demo")
def demo():
    logging.info('chạy /demo')
    demo = { 
        "/" : index(),
        "/get_products": get_products(),
    }
    return demo
    
def main(host='0.0.0.0', port=5000):
    # Khởi tạo và bắt đầu luồng riêng cho lặp lịch
    logging.info('tạo luồng và chạy luồng')
    schedule_thread = threading.Thread(target=run_schedule)
    schedule_thread.start()
    # Chạy ứng dụng Flask
    logging.info('chạy app')
    app.run(host=host, port=port)
    
if __name__ == "__main__":
    logging.info('chạy main')
    main()