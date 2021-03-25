from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")

driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

pim = driver.find_element_by_id("menu_pim_viewPimModule")
add_employee = driver.find_element_by_id("menu_pim_addEmployee")
actions = ActionChains(driver)
actions.move_to_element(pim).move_to_element(add_employee).click().perform()

driver.find_element_by_id("firstName").send_keys("Ashok")
driver.find_element_by_id("middleName").send_keys("Kumar")
driver.find_element_by_id("lastName").send_keys("Reddymasi")

