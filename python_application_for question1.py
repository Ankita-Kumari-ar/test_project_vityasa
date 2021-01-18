import requests
item=[1, 4, -1, "hello", "world", 0, 10, 7]
r=requests.post('https://ankiwebtestintern.herokuapp.com/items',json=item)
print(r.json())

