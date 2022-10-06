from email import header
import requests

url = 'http://localhost:8000/healthz'
data = {}
headers = {}

res = requests.get(url=url,data=data,headers=headers)

print(res.status_code, res.content)