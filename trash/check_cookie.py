import requests

payload = {"login":"secret_login", "password":"secret_pass2"}
responce1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

cookie_value = responce1.cookies.get('auth_cookie')

my_cookies = {}
if cookie_value is not None:
    my_cookies.update({'auth_cookie': cookie_value})

responce2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=my_cookies)

print(responce2.text)