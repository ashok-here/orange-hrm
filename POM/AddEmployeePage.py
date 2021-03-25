from selenium.webdriver.support.ui import Select
import time

class AddEmployeePage:

    txt_FirstName_id = "firstName"
    txt_MiddleName_id = "middleName"
    txt_LastName_id = "lastName"
    btn_Photo_ChooseFile_id = "photofile"
    chkbx_CreateLoginDetails_id = "chkLogin"
    txt_AddEmp_Username_id = "user_name"
    txt_AddEmp_Password_id = "user_password"
    txt_AddEmp_ConfirmPassword_id = "re_password"
    btn_AddEmp_Save_id = "btnSave"
    lbl_FirstName_Required_xpath = "//li[1]/span[text()='Required']"
    lbl_Password_8characters_xpath = "//span[text()='Should have at least 8 characters']"
    btn_PersonalDetails_Edit_xpath = "//input[@value='Edit']"
    radiobtn_Gender_Male_id = "personal_optGender_1"
    cal_DateofBirth_xpath = "//form[@id='frmEmpPersonalDetails']//ol[3]/li[4]/img"
    btn_PersonalDetails_Save_xpath = "//input[@value='Save']"
    link_Job_linktext = "Job"
    btn_Job_Edit_xpath = "//input[@id='btnSave' and @value='Edit']"
    btn_Job_Save_xpath = "//input[@id='btnSave' and @value='Save']"
    link_Reportto_linktext = "Report-to"
    btn_AssignedSupervisors_Add_id = "btnAddSupervisorDetail"
    txt_AddSupervisor_Name_id = "reportto_supervisorName_empName"
    name_autotext_xpath = "/html/body/div[4]/ul/li"
    btn_AddSupervisor_Save_id = "btnSaveReportTo"
    link_EmployeeList_linktext = "Employee List"
    txt_EmployeeName_id = "empsearch_employee_name_empName"
    emp_name_autotext_xpath = "/html/body/div[4]/ul/li"
    btn_Search_id = "searchBtn"

    def __init__(self, driver):
        self.driver = driver

    def enterFirstName(self):
        self.driver.find_element_by_id(self.txt_FirstName_id).send_keys("Ashok")

    def enterMiddleName(self):
        self.driver.find_element_by_id(self.txt_MiddleName_id).send_keys("Kumar")

    def enterLastName(self):
        self.driver.find_element_by_id(self.txt_LastName_id).send_keys("Reddymasi")

    def uploadChooseFile(self):
        time.sleep(2)
        self.driver.find_element_by_id("photofile").send_keys("D://Openpyxl//Spy.PNG")

    def checkCreateLoginDetails(self):
        time.sleep(2)
        self.driver.find_element_by_id(self.chkbx_CreateLoginDetails_id).click()

    def enterUsername(self):
        self.driver.find_element_by_id(self.txt_AddEmp_Username_id).send_keys("Ashok")

    def enterPassword(self):
        self.driver.find_element_by_id(self.txt_AddEmp_Password_id).send_keys("ashok123")

    def enterConfirmPassword(self):
        self.driver.find_element_by_id(self.txt_AddEmp_ConfirmPassword_id).send_keys("ashok123")

    def clickSave(self):
        time.sleep(2)
        self.driver.find_element_by_id(self.btn_AddEmp_Save_id).click()

    def getRequiredLabel(self):
        label_Fname_required = self.driver.find_element_by_xpath(self.lbl_FirstName_Required_xpath).text
        assert label_Fname_required == "Required"
        print(label_Fname_required, " -First name missing label is matching.")

    def getPwd8charsLabel(self):
        label_pwd_8chars = self.driver.find_element_by_xpath(self.lbl_Password_8characters_xpath).text
        assert label_pwd_8chars == "Should have at least 8 characters"
        print(label_pwd_8chars, " -Password missing label is matching.")

    def uncheckCreateLoginDetails(self):
        self.driver.find_element_by_id(self.chkbx_CreateLoginDetails_id).click()

    def clickPersonalDetailsEdit(self):
        time.sleep(3)
        self.driver.find_element_by_xpath(self.btn_PersonalDetails_Edit_xpath).click()

    def selectGender(self):
        time.sleep(2)
        self.driver.find_element_by_id(self.radiobtn_Gender_Male_id).click()

    def selectMaritalStatus(self):
        time.sleep(2)
        drop_down = Select(self.driver.find_element_by_id("personal_cmbMarital"))
        drop_down.select_by_value("Single")

    def selectDOB(self):
        self.driver.find_element_by_xpath(self.cal_DateofBirth_xpath).click()
        time.sleep(2)
        select_year = Select(self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']"))
        select_year.select_by_value("1992")
        time.sleep(2)
        select_month = Select(self.driver.find_element_by_xpath("//select[@class='ui-datepicker-month']"))
        select_month.select_by_visible_text("Jan")
        time.sleep(2)
        select_day = self.driver.find_element_by_xpath("//a[@class='ui-state-default' and text()='3']")
        select_day.click()
        txt_DOB = self.driver.find_element_by_id("personal_DOB").get_attribute('value')
        assert txt_DOB == "1992-01-03", "Selected DOB is not matching."
        print("Selected DOB is: ", txt_DOB)

    def clickPersonalDetailsSave(self):
        self.driver.find_element_by_xpath(self.btn_PersonalDetails_Save_xpath).click()

    def clickJob(self):
        time.sleep(3)
        self.driver.find_element_by_link_text(self.link_Job_linktext).click()

    def clickJobEdit(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.btn_Job_Edit_xpath).click()

    def selectJobTitle(self):
        time.sleep(2)
        job_title = self.driver.find_element_by_id("job_job_title")
        drp_title = Select(job_title)
        drp_title.select_by_visible_text("Software Engineer")

    def selectEmploymentStatus(self):
        time.sleep(2)
        employment_status = self.driver.find_element_by_id("job_emp_status")
        drp_emp_status = Select(employment_status)
        drp_emp_status.select_by_visible_text("Full-Time Permanent")

    def selectSubUnit(self):
        time.sleep(2)
        sub_unit = self.driver.find_element_by_id("job_sub_unit")
        drp_sub_unit = Select(sub_unit)
        drp_sub_unit.select_by_visible_text("Engineering")

    def clickJobSave(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.btn_Job_Save_xpath).click()

    def clickReportto(self):
        time.sleep(3)
        self.driver.find_element_by_link_text(self.link_Reportto_linktext).click()

    def clickAddSupervisorsAdd(self):
        time.sleep(3)
        self.driver.find_element_by_id(self.btn_AssignedSupervisors_Add_id).click()

    def enterAddSupervisorName(self):
        time.sleep(2)
        self.driver.find_element_by_id(self.txt_AddSupervisor_Name_id).send_keys("Paul")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.name_autotext_xpath).click()

    def selectReportingMethod(self):
        reporting_method = self.driver.find_element_by_id("reportto_reportingMethodType")
        drp_report = Select(reporting_method)
        drp_report.select_by_visible_text("Direct")

    def clickAddSupervisorSave(self):
        self.driver.find_element_by_id(self.btn_AddSupervisor_Save_id).click()

    def clickEmployeeList(self):
        time.sleep(2)
        self.driver.find_element_by_link_text(self.link_EmployeeList_linktext).click()

    def enterEmployeeName(self):
        time.sleep(2)
        self.driver.find_element_by_id(self.txt_EmployeeName_id).send_keys("Ash")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.emp_name_autotext_xpath).click()

    def clickSearch(self):
        time.sleep(2)
        self.driver.find_element_by_id(self.btn_Search_id).click()

    def getEmpDetails(self):
        time.sleep(2)
        header = self.driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/div/form/div/table/thead/tr").text
        val = self.driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/div/form/div/table/tbody/tr").text
        print(header)
        print(val)

