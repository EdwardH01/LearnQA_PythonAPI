# Комплексный тест на редактирование профиля юзера (состоит из методов:
# - создание юзера (REGISTER)
# - авторизация под созданным юзером (LOGIN)
# - редактирование его профиля (EDIT)
# - получение данных профиля и сравнение его имени с новым (GET)

#import requests
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure
import time

@allure.epic("Editing cases")
class TestUserEdit(BaseCase):
    @allure.description("This test for successfully editing an already registered user")
    def test_edit_just_created_user(self):
    # REGISTER
        register_data = self.prepare_registration_data()

        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        firstName = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

    # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login/", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

    # EDIT
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 200)

    # GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(response4, "firstName", new_name, "Wrong name of the user after edit")

# Ex17-1
    @allure.description("This is a test of unsuccessful user editing without authorization")
    def test_edit_existing_user_wo_auth(self):
        new_name = "Anna"
        token = "no_token"
        auth_sid = "no_auth_sid"

        response1 = MyRequests.put(
            f"/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response1, 400)

# Ex17-2
    @allure.description("This test checks editing the user profile with logging in as another user")
    def test_edit_user_profile_as_another_user(self):
    # step 1 - REGISTER user#1
        register_data1 = self.prepare_registration_data()

        response1 = MyRequests.post("/user/", data=register_data1)

        Assertions.assert_code_status(response1, 200)
#        Assertions.assert_json_has_key(response1, "id")

        email1 = register_data1['email']
        password1 = register_data1['password']

    # step 2 - REGISTER user#2
        time.sleep(1)   # Дополнительный таймаут, т.к. без него тест проходит через раз
        register_data2 = self.prepare_registration_data()

        response2 = MyRequests.post("/user/", data=register_data2)

        user_id2 = self.get_json_value(response2, "id")

        Assertions.assert_code_status(response2, 200)
#        Assertions.assert_json_has_key(response2, "id")

    # step 3 - LOGIN user#1
        login_data = {
            'email': email1,
            'password': password1
        }

        response3 = MyRequests.post("/user/login/", data=login_data)

        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")

    # step 4 - EDIT user#2
        new_name = "Victor"

        response4 = MyRequests.put(
            f"/user/{user_id2}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response4, 200)

    # step 5 - GET user#2
        response5 = MyRequests.get(
            f"/user/{user_id2}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        unexpected_fields = ["id", "email", "firstName", "lastName"]
        Assertions.assert_json_has_not_keys(response5, unexpected_fields)

# Ex17-3
    @allure.description("This test for unsuccessfully editing registered user email w/o @")
    def test_edit_user_email_without_at(self):
    # step 1 - REGISTER
        register_data = self.prepare_registration_data()

        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

    # step 2 - LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login/", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

    # step 3 - EDIT
        data = self.prepare_registration_data_without_at()

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data=data
        )

        assert response3.text == "Invalid email format", f"Unexpected response content {response3.text}"

# Ex17-4
    @allure.description("This test for unsuccessfully editing registered user with 1 character firstName")
    def test_edit_user_short_firstname(self):
    # step 1 - REGISTER
        register_data = self.prepare_registration_data()

        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

    # step 2 - LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login/", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

    # step 3 - EDIT
        time.sleep(1)  # Дополнительный таймаут, т.к. без него тест проходит через раз
        data = self.prepare_registration_data_with_short_firstname()

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data=data
        )

        Assertions.assert_short_firstname(response3, '{"error":"Too short value for field firstName"}')
