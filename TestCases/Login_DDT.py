import time

import pytest
from selenium.common import TimeoutException
from Utilities.readProperties import readConfig
from PageObjects.LoginPage import Login
from Utilities.customLogger import logGenerator
from Utilities import XLutils


class Test_002_loginDDT:
    url = readConfig.getUrl()
    logger = logGenerator.logGen()
    # ddt = "C:/Users/Anbulingam/PycharmProjects/pythonProjects/TestData/ddt.xlsx"
    path = ".//TestData//ddt.xlsx"

    @pytest.mark.regression
    def test_login_DDT(self, setup):
        try:
            self.logger.info("*******Test002_loginDDT***********")
            self.logger.info("*******Data Driven started**********")
            self.driver = setup
            self.driver.get(self.url)
            self.lp = Login(self.driver)
            self.actual_list = []
            self.rows = XLutils.row_count(self.path, 'credentials')
            for r in range(2, self.rows + 1):
                self.username = XLutils.read_data(self.path, 'credentials', r, 1)
                self.password = XLutils.read_data(self.path, 'credentials', r, 2)
                self.exp = XLutils.read_data(self.path, 'credentials', r, 3)
                # print(f"Reading values from Excel: {self.username}, {self.password}, {self.exp}")
                self.lp.set_username(self.username)
                self.lp.set_password(self.password)
                self.lp.click_login()
                time.sleep(2)
                self.logger.info("*********Trying to login*************")
                # if self.lp.dashboard_ele():
                if "dashboard" in self.driver.current_url:
                    if self.exp == "Pass":
                        self.logger.info("********Passed**********")
                        self.actual_list.append("Pass")
                        XLutils.write_data(self.path, 'credentials', r, 4, 'Pass')
                        XLutils.fill_green(self.path, 'credentials', r, 4)
                        self.lp.click_logout()
                    elif self.exp == "Fail":
                        self.logger.info("***********Failed***********")
                        self.actual_list.append("Fail")
                        XLutils.write_data(self.path, 'credentials', r, 4, 'Fail')
                        XLutils.fill_red(self.path, 'credentials', r, 4)
                        self.lp.click_logout()
                elif "dashboard" not in self.driver.current_url:
                    if self.exp == "Pass":
                        self.logger.info("*********Failed***********")
                        self.actual_list.append("Fail")
                        XLutils.write_data(self.path, 'credentials', r, 4, 'Fail')
                        XLutils.fill_green(self.path, 'credentials', r, 4)
                    elif self.exp == "Fail":
                        self.logger.info("********Passed**********")
                        self.actual_list.append("Pass")
                        XLutils.write_data(self.path, 'credentials', r, 4, 'Pass')
                        XLutils.fill_red(self.path, 'credentials', r, 4)
            if "Fail" not in self.actual_list:
                self.logger.info("*******Data Driven completed*********")
            else:
                self.logger.error("*********Data Driven Failed********")
        except (TimeoutException, Exception) as e:
            print("Error message", e)