from ast import alias
import requests as req

res = req.get("https://api.ipify.org/")

print(res.status_code)
print(res.text)