import requests

payload = {"name": "User_1"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response.text)
