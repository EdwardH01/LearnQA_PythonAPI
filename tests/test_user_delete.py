#Ex18

from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure
import time


@allure.epic("Deleting user profile cases")
class TestUserDelete(BaseCase):
# Ex18-1
    @allure.description("This is a test of unsuccessful deleting user_id = 2")
    def test_delete_user_id_2(self):
        payload = {"email": 'vinkotov@example.com', "password": '1234'}

        response1 = MyRequests.post(
            f"/user/login",
            data=payload
        )

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        Assertions.assert_code_status(response1, 200)

        response2 = MyRequests.delete(
            f"/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        answer = response2.text

        Assertions.assert_code_status(response2, 400)
        assert "Please, do not delete test users with ID 1, 2, 3, 4 or 5." in answer, \
            "Unexpected successful deleting the profile user_id = 2"

# Ex18-2
    @allure.description("This is a test of successful deleting new created user")
    def test_delete_new_created_user(self):
    # REGISTER
        register_data = self.prepare_registration_data()

        response1 = MyRequests.post("/user/", data=register_data)

        email = register_data['email']
        password = register_data['password']
        user_id = response1.json()["id"]

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

    # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login",data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        Assertions.assert_code_status(response2, 200)

    # DELETE
        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response3, 200)

    # READ
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        answer = response4.text
        assert "User not found" in answer, \
            "Unsuccessful deletion of newly created user"

# Ex18-3
    @allure.description("This test checks deleting the user profile with logging in as another user")
    def test_delete_user_as_another_user(self):
    # step 1 - REGISTER user#1
        register_data1 = self.prepare_registration_data()

        response1 = MyRequests.post("/user/", data=register_data1)

        email1 = register_data1['email']
        password1 = register_data1['password']

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

    # step 2 - REGISTER user#2
        time.sleep(1)  # Дополнительный таймаут, т.к. без него тест проходит через раз
        register_data2 = self.prepare_registration_data()

        response2 = MyRequests.post("/user/", data=register_data2)

        user_id2 = self.get_json_value(response2, "id")

    # step 3 - LOGIN user#1
        login_data = {
            'email': email1,
            'password': password1
        }

        response3 = MyRequests.post("/user/login/", data=login_data)

        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")

    # step 4 - DELETE user#2 with credentials of user#1

        response4 = MyRequests.delete(
            f"/user/{user_id2}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response4, 200)

    # step 5 - GET user#2

        response5 = MyRequests.get(
            f"/user/{user_id2}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response5, 200)