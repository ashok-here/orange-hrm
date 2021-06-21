from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")

driver.maximize_window()
driver.get("https://learn.letskodeit.com/p/practice")

Benz_chkbx = driver.find_element_by_id("benzcheck")
Benz_chkbx.click()
print(Benz_chkbx.is_selected())
