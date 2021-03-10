class UsersPage:
    txt_SystemUsername_id = "searchSystemUser_userName"
    btn_Search_id = "searchBtn"
    lbl_NoRecordFound_xpath = "//*[@id='resultTable']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def enter_Username(self, system_username):
        self.driver.find_element_by_id(self.txt_SystemUsername_id).send_keys(system_username)

    def click_Search(self):
        self.driver.find_element_by_id(self.btn_Search_id).click()

    def label_NoRecordsFound(self):
        label = self.driver.find_element_by_xpath(self.lbl_NoRecordFound_xpath).text
        print(label)

