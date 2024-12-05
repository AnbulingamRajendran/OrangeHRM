from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.customLogger import logGenerator
from PageObjects.AddEmpPage import add_emp


class searchEmp:
    logger = logGenerator.logGen()

    empName_xpath = "(//div[@class='oxd-autocomplete-wrapper'])[1]//input[@placeholder='Type for hints...']"
    empID_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
    empStatus_dropdown_xpath = "(//div[@class='oxd-select-text oxd-select-text--active'])[1]//div[@class='oxd-select-text--after']"
    include_dropdown_xpath = "(//div[@class='oxd-select-text oxd-select-text--active'])[2]//div[@class='oxd-select-text--after']"
    jobTitle_dropdown_xpath = "(//div[@class='oxd-select-text oxd-select-text--active'])[3]//div[@class='oxd-select-text--after']"
    subUnit_dropdown_xpath = "(//div[@class='oxd-select-text oxd-select-text--active'])[4]//div[@class='oxd-select-text--after']"
    supervisorName_xpath = "(//div[@class='oxd-autocomplete-wrapper'])[2]//input[@placeholder='Type for hints...']"
    searchButton_xpath = "//button[normalize-space()='Search']"
    resetButton_xpath = "//button[normalize-space()='Reset']"
    table_xpath = "//div[@class='orangehrm-container']"
    tableSearchResults_xpath = "//div[@class='oxd-table-body']"
    tableRows_xpath = "//div[@class='oxd-table-body']//div[@role='row']"
    tableColumns_xpath = "//div[@class='oxd-table-body']//div[@role='cell']"
    editButton_xpath = "//div[@class='oxd-table-body']//div[@role='cell'][9]//button[@type='button'][1]"
    delButton_xpath = "//div[@class='oxd-table-body']//div[@role='cell'][9]//button[@type='button'][1]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.add_Emp = add_emp(self.driver)

    def enter_empName(self, emp_name):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.empName_xpath))).send_keys(emp_name)

    def enter_empID(self, emp_id):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.empName_xpath))).send_keys(emp_id)

    # def select_empStatus(self, option):

    def click_search(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.searchButton_xpath))).click()

    def rows_count(self):
        rows = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.tableRows_xpath)))
        return len(rows)

    def cols_count(self):
        col = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.tableColumns_xpath)))
        return len(col)

    def searchBy_name(self, emp_name):
        matched_names = []
        for r in range(1, self.rows_count() + 1):
            # result = self.wait.until(EC.presence_of_element_located((By.XPATH, self.tableSearchResults_xpath)))
            name = self.wait.until(
                EC.presence_of_element_located((By.XPATH, f"(//div[@class='oxd-table-body']//div[@role='row'])[{r}]//div[@role='cell'][3]"))).text
            last_name = self.wait.until(
                EC.presence_of_element_located((By.XPATH, f"(//div[@class='oxd-table-body']//div[@role='row'])[{r}]//div[@role='cell'][4]"))).text
            print("Received name", name)
            if emp_name.lower() in name.lower():
                fullname = f"{name}{last_name}"
                print("Matched name :", fullname)
                matched_names.append(fullname)
                self.logger.info("*************Name matched**********")
        if matched_names:
            return True
        else:
            self.logger.info("*********name not matching")
            return None


    delete_selectedButton_xpath = "//button[normalize-space()='Delete Selected']"
    yes_deleteButton_xpath = "//button[normalize-space()='Yes, Delete']"
    no_cancelButton_xpath = "//button[normalize-space()='Yes, Delete']"
    alertCloseButton_xpath = "//button[normalize-space()='×']"
    records_xpath = "//span[@class='oxd-text oxd-text--span']"

    def records_getter(self):
        records = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.records_xpath))).text
        return records

    def del_Employee(self, emp_name):
        print("Given name :", emp_name)
        row_count = self.rows_count()
        if row_count == 0:
            self.logger.info("***********NO Records found**************")
            return
        while True:
            matched = False
            for r in range(1, self.rows_count() + 1):
                name = self.wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, f"(//div[@class='oxd-table-body']//div[@role='row'])[{r}]//div[@role='cell'][3]"))).text
                last_name = self.wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, f"(//div[@class='oxd-table-body']//div[@role='row'])[{r}]//div[@role='cell'][4]"))).text
                print("Received name:", name)
                if emp_name.lower() in name.lower():
                    fullname = f"{name}{last_name}"
                    print("Matched name :", fullname)
                    self.logger.info("*************Name matched**********")
                    try:
                        checkbox = self.wait.until(EC.presence_of_element_located((By.XPATH, f"(//i[@class='oxd-icon bi-check oxd-checkbox-input-icon'])[{r}]")))
                        checkbox.click()
                        self.logger.info("***********Employee selected**************")
                        self.wait.until(EC.presence_of_element_located((By.XPATH, self.delete_selectedButton_xpath))).click()
                        self.wait.until(EC.presence_of_element_located((By.XPATH, self.yes_deleteButton_xpath))).click()
                        self.logger.info("************Employee Deleted***************")
                        print("Toaster message: ", self.add_Emp.getToaster_msg())
                        matched = True
                        break
                    except TimeoutException as e:
                        print("Error message:", e)
            if not matched:
                self.logger.info("**************Employee not found*****************")
                print(self.add_Emp.getToaster_msg())










