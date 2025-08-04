import requests

res = requests.get("https://httpbin.org/get")
print(res.status_code)
