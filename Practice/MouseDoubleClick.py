from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")

driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")

CopyText_btn = driver.find_element_by_xpath("//button[text()='Copy Text']")

action = ActionChains(driver)
action.double_click(CopyText_btn).perform()

