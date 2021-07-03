import requests

responce = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
parsed_task = responce.json()
print(parsed_task['token'])
print(parsed_task['seconds'])
