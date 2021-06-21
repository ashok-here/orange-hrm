from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")

driver.maximize_window()
driver.get("https://learn.letskodeit.com/p/practice")

drpdwn_cars = driver.find_element_by_id("carselect")
drp = Select(drpdwn_cars)
drp.select_by_visible_text("Honda")
#drp.select_by_value("honda")
#drp.select_by_index("2")

print("Selected drop down value is:", drpdwn_cars.get_attribute('value'))

