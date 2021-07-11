#Ex12:

import requests

url = "https://playground.learnqa.ru/api/homework_header"

header_keys = [
    ('Date'),
    ('Content-Type'),
    ('Content-Length'),
    ('Connection'),
    ('Keep-Alive'),
    ('Server'),
    ('x-secret-homework-header'),
    ('Cache-Control'),
    ('Expires')
]

print(dict(requests.get(url).headers))

class TestHWHeader:
    def test_get_unexpected_header(self):
        test_get_unexpected_header = requests.get(url).headers
        for key in dict(test_get_unexpected_header).keys():
            assert key in header_keys, f"Unexpected header '{key}'"

    def test_get_exist_header(self):
        test_get_exist_header = requests.get(url).headers
        for i in header_keys:
            assert i in test_get_exist_header, f"Method does not returned header '{i}'"

    def test_get_notempty_header(self):
        test_get_notempty_header = requests.get(url).headers
        for key, value in dict(test_get_notempty_header).items():
            assert value != '', f"Header '{key}' with empty value"
