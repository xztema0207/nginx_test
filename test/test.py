import requests 
MAX_REQUEST = 100
data = {}
for i in range(100):
    res = requests.get("http://127.0.0.1:8000/")
    id = res.json()["id"]
    if data.get(id):
        data[id] = data[id]+1
    else:
        data[id]=1

print(data)