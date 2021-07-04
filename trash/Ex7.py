#Ex7:
import requests

#1
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("1.1. " + str(response.status_code) + ', ' + response.text)
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("1.2. " + str(response.status_code) + ', ' + response.text)
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("1.3. " + str(response.status_code) + ', ' + response.text)
response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("1.4. " + str(response.status_code) + ', ' + response.text)

#2
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"HEAD"})
print("2. " + str(response.status_code) + ', ' + str(response.headers))

#3
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
print("3.1. " + str(response.status_code) + ', ' + response.text)
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"POST"})
print("3.2. " + str(response.status_code) + ', ' + response.text)
response = requests.put("https://playground.learnqa.ru/api/compare_query_type", data={"method":"PUT"})
print("3.3. " + str(response.status_code) + ', ' + response.text)
response = requests.delete("https://playground.learnqa.ru/api/compare_query_type", data={"method":"DELETE"})
print("3.4. " + str(response.status_code) + ', ' + response.text)

#4
meth = ('GET', 'POST', 'PUT', 'DELETE')
for i in meth:
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":i})
    print('Request type: GET, parameter: ' + str(i) + ', ' + str(response.status_code) + ', ' + response.text)

    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":i})
    print('Request type: POST, parameter: ' + str(i) + ', ' + str(response.status_code) + ', ' + response.text)

    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": i})
    print('Request type: PUT, parameter: ' + str(i) + ', ' + str(response.status_code) + ', ' + response.text)

    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": i})
    print('Request type: DELETE, parameter: ' + str(i) + ', ' + str(response.status_code) + ', ' + response.text)