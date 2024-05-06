

from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.get('/')
def home():
    return render_template('index.html')

@app.get('/products')
def crawling_products():
    url = 'http://db_api:5001/list'
    products = requests.get(url).json()
    return products

@app.get('/fetch')
def fetch():
    url = 'http://db_api:5001/fetch'
    res = requests.get(url).json()
    return res

def main(host='0.0.0.0', port=3000):
    app.run(debug=True, host=host, port=port)
    
if __name__ == "__main__":
    main()
