from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")

driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/jquery-dual-list-box-demo.html")

multi_list_box = driver.find_element_by_xpath("//select[@class='form-control pickListSelect pickData']")

list_items = Select(multi_list_box)
list_items.select_by_visible_text("Sophia")
list_items.select_by_visible_text("Valentina")
list_items.select_by_visible_text("Laura")

#Another way is to identify each element and use CONTROLE Keys to select multiple items from List box.
