import requests

url = "https://api.sendo.vn/flash-deal/buyer/ajax-product/"
post = {"limit": 60,"device": "web","is_widget": True,"special_status":0,"source_page":"homepage"}
response = requests.post(url, data=post)
data = response.json()['data']
print(data)