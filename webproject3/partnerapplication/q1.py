import requests
import json
Base_Url='http://127.0.0.1:8000/'
ENDPOINT='items'
item=[1, 4, -1, "hello", "world", 0, 10, 7]
json_data=json.dumps(item)
r=requests.post(Base_Url+ENDPOINT,json_data)
print(r.json())