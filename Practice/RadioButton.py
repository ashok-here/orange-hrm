from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://learn.letskodeit.com/p/practice")

radbtn_BMW_id = "bmwradio"
driver.find_element_by_id(radbtn_BMW_id).click()
radbtn_selected = driver.find_element_by_id(radbtn_BMW_id).is_selected()
print(radbtn_selected)

