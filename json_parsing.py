import json

string_as_json_format = '{"answer": "Hello, user!"}'    # Получение строки в формате json
obj01 = json.loads(string_as_json_format)   # Парсинг строки в json-объект (словарь по своей структуре)
                                            # и передача этого объекта в переменную obj01
key = 'answer'

if key in obj01:
    print(obj01[key])
else:
    print(f"Ключа {key} в JSON нет")
