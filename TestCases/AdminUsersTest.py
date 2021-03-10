from selenium import webdriver
import unittest
import HtmlTestRunner
import time
import sys
sys.path.append("C:/Users/areddymasi/PycharmProjects/orange-hrm")
from POM.LoginPage import LoginPage
from POM.DashboardPage import DashboardPage
from POM.UsersPage import UsersPage


class AdminUsersTest(unittest.TestCase):
    driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")
    url = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"
    system_username = "Test.User"

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

    def test_NavigatetoUsers(self):
        dp = DashboardPage(self.driver)
        dp.clickAdminUsers()

    def test_SearchForInvalidUser(self):
        up = UsersPage(self.driver)
        up.enter_Username(self.system_username)
        up.click_Search()
        up.label_NoRecordsFound()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/areddymasi/PycharmProjects/orange-hrm/Reports"))


