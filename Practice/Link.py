from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")

driver.maximize_window()
driver.get("https://letskodeit.teachable.com/")
print(driver.title)

time.sleep(2)
link_Practice = driver.find_element_by_link_text("Practice")
print("Link name is:", link_Practice.text)

link_Practice.click()
time.sleep(2)
print(driver.title)

driver.close()

