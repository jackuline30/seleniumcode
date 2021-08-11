import pytest
@pytest.mark.reg
def test_login():
    print("Login page")

@pytest.mark.smoke
@pytest.mark.sanity
def test_facebook():
    print("Facebook")

@pytest.mark.smoke
def test_adactin():
    print("adactin")