from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")

driver.maximize_window()
driver.get("https://letskodeit.teachable.com/")

print(driver.title)

