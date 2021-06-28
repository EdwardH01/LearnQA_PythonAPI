import requests

response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1":"value1", "param2":"value2"})
print("1. " + response.text)

response = requests.post("https://playground.learnqa.ru/api/check_type", params={"param1":"value1", "param2":"value2"})
print("2. " + response.text)

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1":"value1", "param2":"value2"})
print("3. " + response.text)
