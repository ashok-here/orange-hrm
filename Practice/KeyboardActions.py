from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")

driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/bootstrap-dual-list-box-demo.html")

bootstrap_item = driver.find_element_by_xpath("//li[text()='bootstrap-duallist ']")
vestibulum_item = driver.find_element_by_xpath("//li[text()='Vestibulum at eros']")

keys_action = ActionChains(driver)

keys_action.key_down(Keys.CONTROL).click(bootstrap_item).click(vestibulum_item).perform()





