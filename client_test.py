import requests
import json

url = "https://mije4kosbd.execute-api.ap-southeast-2.amazonaws.com/default/raspi-input"

data = {'rasp_id' : '1',
        'status': '10'

data1 = json.dumps(data,ensure_ascii=False)
print(data)

r= requests.post(url,data1)
print(r)
