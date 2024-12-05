import os
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.customLogger import logGenerator


class add_emp:
    logger = logGenerator.logGen()

    PIM_xpath = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']"
    AddButton_xpath = "//button[normalize-space()='Add']"
    FirstName_xpath = "//input[@placeholder='First Name']"
    MiddleName_xpath = "//input[@placeholder='Middle Name']"
    LastName_xpath = "//input[@placeholder='Last Name']"
    Empid_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    CreateLoginDetails_xpath = "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
    Username_xpath = "(//input[@class='oxd-input oxd-input--active'])[3]"
    Password_xpath = "//div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']"
    ConfPassword_xpath = "//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']"
    AddPic_xpath = "//button[@class='oxd-icon-button oxd-icon-button--solid-main employee-image-action']"
    SaveButton_xpath = "//button[normalize-space()='Save']"
    CancelButton_xpath = "//button[normalize-space()='Cancel']"
    toaster_xpath = "//div[@id='oxd-toaster_1']//p[2]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def clickPIM_option(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.PIM_xpath))).click()

    def click_AddButton(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.AddButton_xpath))).click()

    def set_EmployeeName(self, first_name, middle_name, last_name):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.FirstName_xpath))).send_keys(first_name)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.MiddleName_xpath))).send_keys(middle_name)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.LastName_xpath))).send_keys(last_name)

    def change_empId(self, id):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Empid_xpath))).clear()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Empid_xpath))).send_keys(id)

    def click_CreateLogin(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.CreateLoginDetails_xpath))).click()

    def set_Credentials(self, username, password, confirm_password):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Username_xpath))).send_keys(username)
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Password_xpath))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.ConfPassword_xpath))).send_keys(confirm_password)

    def click_AddProfile(self, file_location):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.AddPic_xpath))).click()
        time.sleep(2)
        pyautogui.write(file_location)
        pyautogui.press('enter')
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, self.AddPic_xpath))).send_keys(file_location)

    def click_SaveButton(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.SaveButton_xpath))).click()

    def click_CancelButton(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.CancelButton_xpath))).click()

    def getToaster_msg(self):
        try:
            msg = self.wait.until(EC.presence_of_element_located((By.XPATH, self.toaster_xpath)))
            self.logger.info("**********Toaster message presented*********")
            return msg.text
        except Exception as e:
            self.logger.info("**********Toaster not presented*************")
            return None
