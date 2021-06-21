from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")

driver.maximize_window()
driver.get("https://www.seleniumeasy.com/")

driver.refresh()
print(driver.title)

time.sleep(2)
driver.find_element_by_link_text("Demo Website!").click()
print(driver.title)

time.sleep(2)
driver.back()
print(driver.title)

time.sleep(2)
driver.forward()
print(driver.title)

driver.close()

