from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/areddymasi/PycharmProjects/orange-hrm/Drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.w3schools.com/html/html_tables.asp")

rows = len(driver.find_elements_by_xpath("//table[@id='customers']/tbody/tr"))
print("Rows count is: ", rows)

columns = len(driver.find_elements_by_xpath("//table[@id='customers']/tbody/tr/th"))
print("Columns count is: ", columns)


for r in range(2, rows+1):
    for c in range(1, columns+1):
        values = driver.find_element_by_xpath("//table[@id='customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(values, end="  ")
    print()

