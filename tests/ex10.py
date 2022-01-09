import pytest


class TestPhrase:
    def test_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, f"Введенная фраза должна иметь длину менее 15 символов"

