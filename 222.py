import requests

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
