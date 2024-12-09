from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    user_name_xpath = "//input[@name='username']"
    password_xpath = "//input[@placeholder='Password']"
    loginButton_xpath = "//button[normalize-space()='Login']"
    dashboard_xpath = "//h6[normalize-space()='Dashboard']"
    profile_xpath = "//p[@class='oxd-userdropdown-name']"
    logoutButton_xpath = "//ul[@class='oxd-dropdown-menu']//li[4]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def set_username(self, username):
        username_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.user_name_xpath)))
        username_field.clear()
        username_field.send_keys(username)

    def set_password(self, password):
        password_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.password_xpath)))
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.loginButton_xpath)))
        login_button.click()

    def dashboard_ele(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.dashboard_xpath))).is_displayed()

    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.profile_xpath))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.logoutButton_xpath))).click()
