from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")

driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo/sub-menus.html")

right_click_me_btn = driver.find_element_by_xpath("//span[text()='right click me']")
sub_group = driver.find_element_by_xpath("//span[text()='Sub group']")
sub_group_2 = driver.find_element_by_xpath("//span[text()='Sub group 2']")
sub_alpha = driver.find_element_by_xpath("//span[text()='alpha']")

action = ActionChains(driver)
right_click = action.context_click(right_click_me_btn)
right_click.move_to_element(sub_group).move_to_element(sub_group_2).move_to_element(sub_alpha).click().perform()

