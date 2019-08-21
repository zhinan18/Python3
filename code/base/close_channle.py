import requests
import json

url_json = 'http://httpbin.org/post'
data_json = json.dumps({'key1': 'value1', 'key2': 'value2'})  # dumps：将python对象解码为json数据
r_json = requests.post(url_json, data_json)
print(r_json)
print(r_json.text)
print(r_json.content)

