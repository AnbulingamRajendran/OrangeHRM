import time

import pytest
from selenium.common import TimeoutException
from Utilities.readProperties import readConfig
from PageObjects.LoginPage import Login
from Utilities.customLogger import logGenerator


class Test_001_login:
    url = readConfig.getUrl()
    username = readConfig.getUsername()
    password = readConfig.getPassword()
    logger = logGenerator.logGen()

    def test_title_check(self, setup):
        self.logger.info("**********Test001_login**********")
        self.logger.info("***********Setting up the driver*********")
        self.driver = setup
        self.driver.get(self.url)
        time.sleep(3)
        self.logger.info("*********Checking the Title**********")
        act_title = self.driver.title
        if act_title == "OrangeHRM":
            print("Title matched")
            self.logger.info("*********Title Matched**********")
        else:
            self.logger.error("*******Title not matched********")

    @pytest.mark.sanity
    def test_login_check(self, setup):
        self.logger.info("***********Setting up the driver*********")
        self.driver = setup
        self.driver.get(self.url)
        self.lp = Login(self.driver)
        try:
            self.logger.info("*********Trying to Login*********")
            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()
            if "dashboard" in self.driver.current_url.lower():
                self.logger.info("**********Login Passed************")
                self.lp.click_logout()
                self.logger.info("*******Logged out***********")
                time.sleep(2)
            else:
                self.logger.error("*************Login Failed*********")
                self.driver.save_screenshot(".//Screenshots//" + "test_login_check.png")
                self.logger.info("********Screenshot taken*************")
                assert False, "Login Failed"
            print("Login passed")
        except TimeoutException as e:
            print("Timeout error", e)
        finally:
            time.sleep(2)
