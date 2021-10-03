# import requests

from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

@allure.epic("Getting user profile cases")
class TestUserGet(BaseCase):
    @allure.description("This test checks getting a user profile w/o logging in as a user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_user_details_not_auth(self):
        response = MyRequests.get("/user/2")
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    @allure.description("This test checks getting the user profile with logging in as a user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_user_details_auth_as_same_user(self):  # Тест для проверки получения профиля авторизованного юзера
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        with allure.step('step 1. Login under user'):
            response1 = MyRequests.post("/user/login", data = data)
            auth_sid = self.get_cookie(response1, "auth_sid")
            token = self.get_header(response1, "x-csrf-token")
            user_id_from_auth_metod = self.get_json_value(response1, "user_id")

        with allure.step('step 2. Getting user profile'):
            response2 = MyRequests.get(
                f"/user/{user_id_from_auth_metod}",
                headers = {"x-csrf-token": token},
                cookies = {"auth_sid": auth_sid}
            )

            expected_fields = ["username", "email", "firstName", "lastName"]
            Assertions.assert_json_has_keys(response2, expected_fields)

# Ex16
    @allure.description("This test checks getting the user profile with logging in as another user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_user_details_auth_as_another_user(self):
        with allure.step('step 1. Registration new user'):
            data = self.prepare_registration_data_ex16()

            response1 = MyRequests.post("/user/", data=data)

            Assertions.assert_code_status(response1, 200)
            Assertions.assert_json_has_key(response1, "id")
            user_id = response1.json()["id"]    # Используется для дебага теста

        with allure.step('step 2. Login under user'):
            response2 = MyRequests.post("/user/login", data=data)
            auth_sid = self.get_cookie(response2, "auth_sid")
            token = self.get_header(response2, "x-csrf-token")

        with allure.step('step 3. Trying to get profile of another user'):
            response3 = MyRequests.get(
                f"/user/2",
                headers = {"x-csrf-token": token},
                cookies = {"auth_sid": auth_sid}
            )
            answer = response3.text

            Assertions.assert_json_has_key(response3, "username")
            assert "id" not in answer, "Unexpected successful getting the user profile on behalf of another user"
