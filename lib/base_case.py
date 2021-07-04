#Ex14(1)

import json.decoder

from requests import Response

class BaseCase:
    # Метод для получения cookie из ответов сервера по имени юзера
    # Сначала в метод передается объект ответа на запрос и имя, по которому из этого ответа получаются cookie.
    # Метод будет проверять - есть ли эти данные в ответе, и если нет - падать, а если есть - возвращать их
    def get_cookie (self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Can't find cookie named {cookie_name} in the last response"
        return response.cookies[cookie_name]

    # Метод для получения заголовков из ответов сервера по имени юзера
    def get_header (self, response: Response, headers_name):
        assert headers_name in response.headers, f"Can't find header named {header_name} in the last response"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}"

        return response_as_dict[name]
