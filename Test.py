from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")
url = "https://opensource-demo.orangehrmlive.com/"
username = "Admin"
password = "admin123"
system_username = "Test.User"

txt_username_name = "txtUsername"
txt_password_name = "txtPassword"
btn_login_id = "btnLogin"
tab_Admin_id = "menu_admin_viewAdminModule"
submenu_UserManagement_id = "menu_admin_UserManagement"
submenu_Users_id = "menu_admin_viewSystemUsers"

txt_SystemUsername_id = "searchSystemUser_userName"
btn_Search_id = "searchBtn"
lbl_NoRecordFound_xpath = "//*[@id='resultTable']/tbody/tr/td"

driver.maximize_window()
driver.get(url)

driver.find_element_by_name(txt_username_name).send_keys(username)
driver.find_element_by_name(txt_password_name).send_keys(password)
driver.find_element_by_id(btn_login_id).click()

action = ActionChains(driver)
admin = driver.find_element_by_id(tab_Admin_id)
user_management = driver.find_element_by_id(submenu_UserManagement_id)
users = driver.find_element_by_id(submenu_Users_id)
action.move_to_element(admin).move_to_element(user_management).move_to_element(users).click().perform()
driver.find_element_by_id(txt_SystemUsername_id).send_keys(system_username)
driver.find_element_by_id(btn_Search_id).click()
label = driver.find_element_by_xpath(lbl_NoRecordFound_xpath).text
print(label)
