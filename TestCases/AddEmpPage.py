import time

import pytest

from PageObjects.AddEmpPage import add_emp
from PageObjects.LoginPage import Login
from Utilities.customLogger import logGenerator
from Utilities.readProperties import readConfig


class Test_003_addEmp:
    url = readConfig.getUrl()
    username = readConfig.getUsername()
    password = readConfig.getPassword()
    logger = logGenerator.logGen()

    @pytest.mark.sanity
    def test_addEmp(self, setup):
        self.first_name = "jon"
        self.middle_name = "eddie"
        self.last_name = "snow"
        self.id = "5"
        self.usr_name = "testerjon"
        self.user_pwd = "Test@123"
        self.conf_pwd = "Test@123"
        self.file_loc = "D:\PycharmProjects\profilepic.jpg"
        try:
            self.logger.info("*********Test003_addemp  started***********")
            self.logger.info("**********Logging in***************")
            self.driver = setup
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.lp = Login(self.driver)
            self.add_emp = add_emp(self.driver)
            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()
            assert "dashboard" in self.driver.current_url.lower(), self.logger.error(
                "**********Login failed***********")
            self.logger.info("*******Logged in*************")
            self.add_emp.clickPIM_option()
            self.add_emp.click_AddButton()
            self.add_emp.set_EmployeeName(self.first_name, self.middle_name, self.last_name)
            self.add_emp.change_empId(self.id)
            self.logger.info("**********Employee name added*************")
            self.add_emp.click_CreateLogin()
            self.add_emp.set_Credentials(self.usr_name, self.user_pwd, self.conf_pwd)
            self.logger.info("**********Credits added*************")
            self.add_emp.click_AddProfile(self.file_loc)
            self.logger.info("********Profile pic added*********")
            self.add_emp.click_SaveButton()
            self.logger.info("**********USER ADDED Successfully****************")
            msg = self.add_emp.getToaster_msg()
            if msg:
                print(f"Toaster message", {msg})
            else:
                print("No toaster message")
        except Exception as e:
            self.logger.info("***********GOT SOME ERROR***********")
            print("Error message: ", e)
        finally:
            time.sleep(10)
            self.driver.save_screenshot(".//Screenshots//" + "test_addEmpCheck.png")
            self.logger.info("*********SCREENSHOT TAKEN*************")
