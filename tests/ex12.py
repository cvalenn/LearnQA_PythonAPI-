import requests


class TestHeaders:
    def test_headers(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response.headers)
        assert ('x-secret-homework-header', 'Some secret value') in response.headers.items(), f"Headers is not valid"