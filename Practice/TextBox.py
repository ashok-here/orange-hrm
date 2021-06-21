from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")

driver.maximize_window()
driver.get("https://learn.letskodeit.com/p/practice")

txt_enter_name_xpath = driver.find_element_by_xpath("//input[@id='name' and @name='enter-name']")
txt_enter_name_xpath.send_keys("Ashok")
name = txt_enter_name_xpath.get_attribute('value')
print("Entered name is:", name)
