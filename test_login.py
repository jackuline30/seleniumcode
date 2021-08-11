import pytest
from selenium import webdriver

class TestFacebook:
    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome(executable_path=r"C:\Users\Beaula Jackuline\pytestprojectnew\Drivers\chromedriver_win32 (3)\chromedriver.exe")
        self.driver.get("https://en-gb.facebook.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield

        self.driver.quit()

    def test_sigin(self,setup):
        txt_email=self.driver.find_element_by_name("email")
        txt_email.send_keys("python@gmail.com")
        txt_password=self.driver.find_element_by_name("pass")
        txt_password.send_keys("selenium")
        button=self.driver.find_element_by_name("login")
        button.click()

