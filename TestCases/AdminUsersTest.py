from selenium import webdriver
import unittest
import HtmlTestRunner
import time
import sys
sys.path.append("C:/Users/areddymasi/PycharmProjects/orange-hrm")
from POM.LoginPage import LoginPage
from POM.DashboardPage import DashboardPage
from POM.UsersPage import UsersPage
from POM.AddUserPage import AddUser


class AdminUsersTest(unittest.TestCase):
    driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")
    url = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"
    system_username = "Test.User"
    user_role = "Admin"
    enter_employee_name = "Pa"
    add_username = "Tester"
    add_password = "tester@123"

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        cls.driver.get(cls.url)

    def test_01_Login(self):
        lp = LoginPage(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(2)
        self.assertEqual("OrangeHRM", self.driver.title, "Webpage title is not matching")
        print(self.driver.title)

    def test_02_NavigatetoUsers(self):
        dp = DashboardPage(self.driver)
        dp.clickAdminUsers()

    def test_03_SearchForInvalidUser(self):
        up = UsersPage(self.driver)
        up.enter_Username(self.system_username)
        up.click_Search()
        time.sleep(2)
        up.label_NoRecordsFound()
        time.sleep(1)
        up.click_Reset()
        time.sleep(1)
        up.click_Add()

    def test_04_AddUser(self):
        au = AddUser(self.driver)
        au.get_label_AddUser()
        au.select_UserRole()
        au.enter_EmployeeName()
        au.enter_Username()
        au.enter_Password()
        au.enter_ConfirmPassword()
        au.click_Save()
        au.verify_AddedUser()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/areddymasi/PycharmProjects/orange-hrm/Reports"))


