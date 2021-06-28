import requests
#1
response = requests.post("https://playground.learnqa.ru/api/check_type")
print("1. ", response.status_code)
#2
response = requests.post("https://playground.learnqa.ru/api/get_500")
print("2. ", response.status_code)
print(response.text)
#3
response = requests.post("https://playground.learnqa.ru/api/something")
print("3. ", response.status_code)
print(response.text)
#4.1
response = requests.post("https://playground.learnqa.ru/api/get_301")
print("4.1. ", response.status_code)
#4.2
response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
print("4.2. ", response.status_code)
#4.3
response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
print("4.3. ", response.status_code)
#5.
response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response.history[0]
second_response = response
print("5. ", first_response.url)
print(second_response.url)
