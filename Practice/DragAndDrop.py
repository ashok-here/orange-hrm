from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index")

source_element = driver.find_element_by_id("draggable")
target_element = driver.find_element_by_id("droptarget")
print("Before drag:", target_element.text)

time.sleep(3)
action = ActionChains(driver)
action.drag_and_drop(source_element, target_element).perform()

time.sleep(2)
print("After drag:", target_element.text)

# Another website example
# driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
#
# source_element = driver.find_element_by_xpath("//div[@id='box3' and text()='Washington']")
# target_element = driver.find_element_by_xpath("//div[@id='box103' and text()='United States']")
#
# time.sleep(3)
# action = ActionChains(driver)
# action.drag_and_drop(source_element, target_element).perform()


