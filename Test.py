from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")
url = "https://opensource-demo.orangehrmlive.com/"
username = "Admin"
password = "admin123"

txt_username_name = "txtUsername"
txt_password_name = "txtPassword"
btn_login_id = "btnLogin"
tab_Admin_id = "menu_admin_viewAdminModule"
submenu_UserManagement_id = "menu_admin_UserManagement"
submenu_Users_id = "menu_admin_viewSystemUsers"

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
#Scroll down by pixel value.
#driver.execute_script("window.scrollBy(0,1000)")
#Scroll down to the end of the page
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#Scroll down the page till element is visible
element = driver.find_element_by_xpath("//a[text()='TestAdmin']")
driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(2)
driver.save_screenshot("./Screenshots/New_User_Added.png")
#driver.get_screenshot_as_file("./Screenshots/New_User_Added.png")


