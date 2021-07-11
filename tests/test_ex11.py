#Ex11:

import requests

url = "https://playground.learnqa.ru/api/homework_cookie"

cookie_keys = ['HomeWork']

print(requests.get(url).cookies)

class TestHomeworkCookie:
    def test_get_unexpected_cookie(self):
        test_get_unexpected_cookie = requests.get(url).cookies
        for key in dict(test_get_unexpected_cookie).keys():
            assert key in cookie_keys, f"Unexpected cookie '{key}'"

    def test_get_exist_cookie(self):
        test_get_exist_cookie = requests.get(url).cookies
        for i in cookie_keys:
            assert i in test_get_exist_cookie, f"Method does not returned cookie '{i}'"

    def test_get_notempty_cookie(self):
        test_get_notempty_cookie = requests.get(url).cookies
        for key, value in dict(test_get_notempty_cookie).items():
            assert value != '', f"Cookie '{key}' with empty value"
