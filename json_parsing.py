import json

string_as_json_format = '{"answer": "Hello, user!"}'
obj01 = json.loads(string_as_json_format)

key = 'answer'

if key in obj01:
    print(obj01[key])
else:
    print(f"Ключа {key} в JSON нет")
