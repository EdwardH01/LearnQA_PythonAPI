import requests

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
#response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":i})
print(response.text)



