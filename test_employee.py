import pytest
class Testc:
    @pytest.mark.smoke
    def test_login(self):
        print("login")

    def test_facebook(self):
        print("facebook")
