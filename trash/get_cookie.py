import requests

payload = {"login":"secret_login", "password":"secret_pass"}
responce = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

print(responce.text)
print(responce.status_code)
print(dict(responce.cookies))
print(responce.headers)