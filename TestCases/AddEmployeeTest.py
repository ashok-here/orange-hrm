from selenium import webdriver
import unittest
import HtmlTestRunner
import time
import sys
sys.path.append("C:/Users/areddymasi/PycharmProjects/orange-hrm")
from POM.LoginPage import LoginPage
from POM.DashboardPage import DashboardPage
from POM.AddEmployeePage import AddEmployeePage


class AddEmployeeTest(unittest.TestCase):
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

    def test_02_NavigatePIMAddEmp(self):
        dp = DashboardPage(self.driver)
        dp.clickPIMAddEmp()

    def test_03_BlankAddEmp(self):
        aep = AddEmployeePage(self.driver)
        aep.checkCreateLoginDetails()
        aep.clickSave()
        aep.getRequiredLabel()
        aep.getPwd8charsLabel()
        aep.uncheckCreateLoginDetails()

    def test_04_AddEmp(self):
        aep = AddEmployeePage(self.driver)
        aep.enterFirstName()
        aep.enterMiddleName()
        aep.enterLastName()
        aep.uploadChooseFile()
        aep.checkCreateLoginDetails()
        aep.enterUsername()
        aep.enterPassword()
        aep.enterConfirmPassword()
        aep.clickSave()

    def test_05_AddPersonalDetails(self):
        aep = AddEmployeePage(self.driver)
        aep.clickPersonalDetailsEdit()
        aep.selectGender()
        aep.selectMaritalStatus()
        aep.selectDOB()
        aep.clickPersonalDetailsSave()

    def test_06_AddJobDetails(self):
        aep = AddEmployeePage(self.driver)
        aep.clickJob()
        aep.clickJobEdit()
        aep.selectJobTitle()
        aep.selectEmploymentStatus()
        aep.selectSubUnit()
        aep.clickJobSave()

    def test_07_AddReportingDetails(self):
        aep = AddEmployeePage(self.driver)
        aep.clickReportto()
        aep.clickAddSupervisorsAdd()
        aep.enterAddSupervisorName()
        aep.selectReportingMethod()
        aep.clickAddSupervisorSave()

    def test_08_SearchEmployeeList(self):
        aep = AddEmployeePage(self.driver)
        aep.clickEmployeeList()
        aep.enterEmployeeName()
        aep.clickSearch()
        aep.getEmpDetails()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/areddymasi/PycharmProjects/orange-hrm/Reports"))


