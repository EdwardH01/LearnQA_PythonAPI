import requests

header1 = {"some_header":"123"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers = header1)
print(response.text)