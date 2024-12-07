import time

import pytest

from Utilities.customLogger import logGenerator
from Utilities.readProperties import readConfig
from PageObjects.SearchEmpPage import searchEmp
from PageObjects.AddEmpPage import add_emp
from PageObjects.LoginPage import Login


class Test_005_deleteEmp:
    url = readConfig.getUrl()
    username = readConfig.getUsername()
    password = readConfig.getPassword()
    logger = logGenerator.logGen()

    @pytest.mark.regression
    def test_deleteEmp(self, setup):
        # self.emp_name = input("enter the employee name for delete: ")
        self.emp_name = "jon"
        try:
            self.logger.info("***********Test005_deleteEmp started*************")
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
            print(self.search_ep.records_getter())
            print("Number of rows", self.search_ep.rows_count())
            self.search_ep.del_Employee(self.emp_name)
            self.logger.info("***********Delete_Employee completed****************")
        except Exception as e:
            print("Error message", e)
        finally:
            self.driver.save_screenshot(".//Screenshots//" + "delete_Employee.png")
            self.logger.info("*********Screenshot taken***************")
            time.sleep(2)


            #pytest -v -s TestCases/DeleteEmp.py --html=./Reports/deleteEmp.html

