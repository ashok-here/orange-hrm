from selenium import webdriver
import unittest
import HtmlTestRunner
import time
import sys
sys.path.append("C:/Users/areddymasi/PycharmProjects/orange-hrm")
from POM.LoginPage import LoginPage


class LoginTest(unittest.TestCase):
    driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")
    url = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        cls.driver.get(cls.url)

    def test_Login(self):
        lp = LoginPage(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(2)
        self.assertEqual("OrangeHRM", self.driver.title, "Webpage title is not matching")
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/areddymasi/PycharmProjects/orange-hrm/Reports"))
