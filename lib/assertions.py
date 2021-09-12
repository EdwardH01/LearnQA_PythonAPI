#Ex14(2)

from requests import Response
import json

class Assertions:
    @staticmethod   # Аннотация для статических методов
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Assertions - assert_json_value_by_name. Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):  # Вариант 1 - Метод проверки наличия одного из полей в ответе сервера
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):   # Вариант 2 - Метод проверки наличия всех полей из списка в ответе сервера
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
        for name in names:
            assert name in response_as_dict, f"Assertions - assert_json_has_keys. Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):  # Метод проверки отсутствия некоторых полей в ответе сервера
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'. But it's present"

        assert name not in response_as_dict, f"Response JSON shouldn't have key '{name}'"

    @staticmethod
    def assert_json_has_not_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'. But it's present"
        for name in names:
            assert name not in response_as_dict, f"Assertions - assert_json_has_not_keys. Response JSON unexpectedly have key '{name}'"


    @staticmethod
    def assert_code_status(response: Response, expected_status_code):   # Метод проверки соответствия статус-кода ожидаемому
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}. Actual: {response.status_code}"

# Ex15-1:
    @staticmethod
    def assert_email_format(response: Response, expected_response_text):   # Метод проверки соответствия ответа сервера
        assert response.text == expected_response_text, \
            f"Unexpected response! Expected: {expected_response_text}. Actual: {response.text}"

# Ex15-3:
    @staticmethod
    def assert_short_name(response: Response, expected_response_text):
        assert response.text == expected_response_text, \
            f"Unexpected success registration with too short username! Expected response: {expected_response_text}. Actual: {response.text}"

# Ex15-4:
    @staticmethod
    def assert_too_long_name(response: Response, expected_response_text):
        assert response.text == expected_response_text, \
            f"Unexpected success registration with too long username! Expected response: {expected_response_text}. Actual: {response.text}"

# Ex17-4:
    @staticmethod
    def assert_short_firstname(response: Response, expected_response_text):
        assert response.text == expected_response_text, \
            f"Unexpected success editing with too short username! Expected response: {expected_response_text}. Actual: {response.text}"

