import requests
headers={
    'Content-type':'application/json', 
    'Accept':'application/json'
}
print("GET:")
res = requests.get("http://127.0.0.1:3000/api/courses/0")
print(res.json())
print("GET:")
res = requests.get("http://127.0.0.1:3000/api/courses/0")
print(res.json())
print("DELETE:")
res = requests.delete("http://127.0.0.1:3000/api/courses/2")
print("POST:")
res = requests.post("http://127.0.0.1:3000/api/courses/3", json = {"name" : "Biology", "videos" : 20}, headers = headers)
print("GET:")
res = requests.get("http://127.0.0.1:3000/api/courses/0")
print(res.json())
print("PUT:")
res = requests.post("http://127.0.0.1:3000/api/courses/1", json = {"name" : "Math", "videos" : 74}, headers = headers)
print(res.json())