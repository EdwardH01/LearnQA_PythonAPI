import requests

class TestHomeworkCookie:
    def test_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"

        response = requests.get(url)
        print(response.status_code)
        print(response.text)

