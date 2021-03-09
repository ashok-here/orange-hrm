class LoginPage:
    txt_username_name = "txtUsername"
    txt_password_name = "txtPassword"
    btn_login_id = "btnLogin"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_name(self.txt_username_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_name(self.txt_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.btn_login_id).click()


