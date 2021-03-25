from selenium.webdriver import ActionChains


class DashboardPage:
    tab_Admin_id = "menu_admin_viewAdminModule"
    submenu_UserManagement_id = "menu_admin_UserManagement"
    submenu_Users_id = "menu_admin_viewSystemUsers"
    tab_PIM_id = "menu_pim_viewPimModule"
    submenu_AddEmployee_id = "menu_pim_addEmployee"

    def __init__(self, driver):
        self.driver = driver

    def clickAdminUsers(self):
        admin = self.driver.find_element_by_id(self.tab_Admin_id)
        user_management = self.driver.find_element_by_id(self.submenu_UserManagement_id)
        users = self.driver.find_element_by_id(self.submenu_Users_id)
        actions = ActionChains(self.driver)
        actions.move_to_element(admin).move_to_element(user_management).move_to_element(users).click().perform()

    def clickPIMAddEmp(self):
        pim = self.driver.find_element_by_id(self.tab_PIM_id)
        add_employee = self.driver.find_element_by_id(self.submenu_AddEmployee_id)
        actions = ActionChains(self.driver)
        actions.move_to_element(pim).move_to_element(add_employee).click().perform()
