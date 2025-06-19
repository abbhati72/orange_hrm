from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login_Page_class:
    username_xpath = "//input[@name='username']"
    password_xpath = "//input[@name='password']"
    login_btn_xpath = "//button[@type='submit']"
    dashboard_text_xpath = "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 4)



    def enterusername(self, username):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.username_xpath)))
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def enterpassword(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def verify_login(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,self.dashboard_text_xpath)))
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.dashboard_text_xpath)))
            return "pass"
        except:
            return "fail"
