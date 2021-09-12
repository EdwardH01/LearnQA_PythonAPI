#Ex14(1)

import json.decoder
import random
import string

from requests import Response
from datetime import datetime

class BaseCase:
    # Метод для получения cookie из ответов сервера по имени юзера
    # Сначала в метод передается объект ответа на запрос и имя, по которому из этого ответа получаются cookie.
    # Метод будет проверять - есть ли эти данные в ответе, и если нет - падать, а если есть - возвращать их
    def get_cookie (self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Can't find cookie named {cookie_name} in the last response"
        return response.cookies[cookie_name]

    # Метод для получения заголовков из ответов сервера по имени юзера
    def get_header (self, response: Response, headers_name):
        assert headers_name in response.headers, f"Can't find header named {headers_name} in the last response"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

        return response_as_dict[name]

    def prepare_registration_data(self, email = None):    # Метод подготовки регистрационных данных юзера
        if email is None:
            base_part = "learnqa"   # Рандомизация email (что-бы после каждого запуска теста в БД всегда сохранялся уникальный email)
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        return {
            'username': 'learnqa',
            'password': '123',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

    def prepare_registration_data_without_at(self, email = None):    # Регистрационные данные юзера без символа @
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}{domain}"
        return {
            'username': 'learnqa',
            'password': '123',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

    def prepare_registration_data_with_short_name(self, email = None):    # Регистрационные данные юзера с именем в 1 символ
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        return {
            'username': 'A',
            'password': '123',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

    def prepare_registration_data_with_too_long_name(self, email = None):    # Регистрационные данные юзера с именем > 250 символов
        def too_long_name(length):  # Функция генерации длинного имени юзера
            chars = string.ascii_lowercase
            random_chars = ''.join(random.choice(chars) for i in range(length))
            return (random_chars)
        username = too_long_name(251)

        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        return {
            'username': username,
            'password': '123',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

    def prepare_registration_data_ex16(self, email = None):    # Метод подготовки регистрационных данных юзера
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        return {
            'username': 'learnqa',
            'password': '0000',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

    def prepare_registration_data_with_short_firstname(self, email = None):    # Регистрационные данные юзера с именем в 1 символ
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        return {
            'username': 'learnqa',
            'password': '123',
            'firstName': 'q',
            'lastName': 'learnqa',
            'email': email
        }
