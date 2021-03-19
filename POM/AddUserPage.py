from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class AddUser:
    #label_AddUser_xpath = '//h1[@id="UserHeading"]'
    drp_UserRole_id = "systemUser_userType"
    txt_EmployeeName_xapth = '//*[@id="systemUser_employeeName_empName"]'
    txt_Username_xpath = '//input[@id="systemUser_userName"]'
    txt_Password_xpath = '//input[@id="systemUser_password"]'
    txt_ConfirmPassword_xpath = '//input[@id="systemUser_confirmPassword"]'
    btn_Save_xpath = '//input[@id="btnSave"]'

    def __init__(self, driver):
        self.driver = driver

    def get_label_AddUser(self):
        wait = WebDriverWait(self.driver, 10)
        lab = wait.until(EC.presence_of_element_located((By.XPATH, '//h1[@id="UserHeading"]'))).text
        print(lab)

    def select_UserRole(self):
        item = Select(self.driver.find_element(By.ID, self.drp_UserRole_id))
        item.select_by_visible_text("Admin")

    def enter_EmployeeName(self):
        self.driver.find_element(By.XPATH, self.txt_EmployeeName_xapth).send_keys("P")
        time.sleep(1)
        action = ActionChains(self.driver)
        action.key_down(Keys.DOWN).key_down(Keys.ENTER).perform()

    def enter_Username(self):
        self.driver.find_element(By.XPATH, self.txt_Username_xpath).send_keys("Tester")

    def enter_Password(self):
        self.driver.find_element(By.XPATH, self.txt_Password_xpath).send_keys("test@123")

    def enter_ConfirmPassword(self):
        self.driver.find_element(By.XPATH, self.txt_ConfirmPassword_xpath).send_keys("test@123")

    def click_Save(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_Save_xpath).click()

    def verify_AddedUser(self):
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//a[text()='Tester']")
        #Scroll down
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        #Take screenshot of newly added user.
        self.driver.save_screenshot("C://Users//areddymasi//PycharmProjects//orange-hrm//Screenshots//New_User_Admin.png")



