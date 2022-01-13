import pytest
import requests


class TestCookies:

    def test_cookies(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(response.cookies)
        assert ('HomeWork', 'hw_value') in response.cookies.items(), f"Cookie is not valid"