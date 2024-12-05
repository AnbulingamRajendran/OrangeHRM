import time

import pytest

from Utilities.customLogger import logGenerator
from Utilities.readProperties import readConfig
from PageObjects.SearchEmpPage import searchEmp
from PageObjects.AddEmpPage import add_emp
from PageObjects.LoginPage import Login


class Test_004_searchEmp:
    url = readConfig.getUrl()
    username = readConfig.getUsername()
    password = readConfig.getPassword()
    logger = logGenerator.logGen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_SearchEmp(self, setup):
        self.emp_name = input("Enter the employee name: ")
        try:
            self.logger.info("***********Test004_searchEmp started*************")
            self.driver = setup
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.lp = Login(self.driver)
            self.logger.info("***********Logging IN*************")
            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()
            self.logger.info("***********Login success*************")
            self.add_ep = add_emp(self.driver)
            self.add_ep.clickPIM_option()
            self.search_ep = searchEmp(self.driver)
            self.logger.info("***********Entering Emp-name*************")
            self.search_ep.enter_empName(self.emp_name)
            self.search_ep.click_search()
            time.sleep(2)
            print(self.search_ep.records_getter())
            if self.search_ep.searchBy_name(self.emp_name):
                print("pass")
            else:
                print("Fail")
        except Exception as e:
            print("Error message", e)
        finally:
            self.driver.save_screenshot(".//Screenshots//" + "test_SearchEmp.png")
            self.logger.info("*********Screenshot taken***************")
            self.logger.info("*********SearchEmp completed***************")
            time.sleep(6)


# pytest -v -s --html=./Reports/SearchEmp.html TestCases/SearchEmp.py




