import requests
import json

url = "http://10.0.0.49:5000/hello"

data = {'Sample Data': 'Hi'}

data1 = json.dumps(data,ensure_ascii=False)
print(data)

r= requests.post(url,data1)
print(r)
