# Тест на регистрацию нового юзера
import pytest
import datetime

from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

@allure.epic("Registration cases")
class TestUserRegister(BaseCase):       # Новый класс - наследник класса BaseCase

    @allure.description("This test checks successfully registration user with unique email")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("This test checks registering user with already existing email")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"
# .decode("utf-8") - перекодировка b-string (b-строки) из последовательности байтов в представление с кодировкой в utf-8

# Ex15-1:
    @allure.description("This test checks registering user with email w/o @")
    @allure.severity(allure.severity_level.MINOR)
    def test_create_user_with_email_without_at(self):
        data = self.prepare_registration_data_without_at()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        Assertions.assert_email_format(response, "Invalid email format")
        assert response.text == "Invalid email format", f"Unexpected response content {response.text}"

# Ex15-2:
    payload = [
        (
            {
                "firstName": "John0",
                "lastName": "Smith0",
                "email": f"user" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + "@example.com",
                "password": "12345"
            }
        ),
        (
            {
                "username": "user1",
                "lastName": "Smith1",
                "email": f"user" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + "@example.com",
                "password": "12345"
            }
        ),
        (
            {
                "username": "user2",
                "firstName": "John2",
                "email": f"user" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + "@example.com",
                "password": "12345"
            }
        ),
        (
            {
                "username": "user3",
                "firstName": "John3",
                "lastName": "Smith3",
                "password": "12345"
            }
        ),
        (
            {
                "username": "user4",
                "firstName": "John4",
                "lastName": "Smith4",
                "email": f"user" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + "@example.com"
            }
        )
    ]
    @allure.description("This test checks that a user cannot register without any of the required fields")
    @pytest.mark.parametrize('payload', payload)
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_without_one_of_required_fields(self, payload):

        response = MyRequests.post("/user/", data=payload)

        answer1 = response.status_code
        answer2 = response.text

        assert answer1 == 400, "Unexpected status code"
        assert "id" not in answer2, "Unexpected successful registration w/o one of the required fields"

# Ex15-3:
    @allure.description("This test checks registering user with 1 character name")
    @allure.severity(allure.severity_level.MINOR)
    def test_create_user_with_short_name(self):
        data = self.prepare_registration_data_with_short_name()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_short_name(response, "The value of 'username' field is too short")

# Ex15-4:
    @allure.description("This test checks registering user with > 250 characters name")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_create_user_with_too_long_name(self):
        data = self.prepare_registration_data_with_too_long_name()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_too_long_name(response, "The value of 'username' field is too long")
