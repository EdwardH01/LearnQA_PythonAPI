#Ex6:
import requests

response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
print(len(response.history))

response_last_url = response.history[len(response.history) - 1]
print(response_last_url.url)
