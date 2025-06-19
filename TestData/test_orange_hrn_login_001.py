import os
import sys
import time
from datetime import datetime

import allure
import pytest
from selenium import webdriver

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PageObjects.Login_Page import Login_Page_class
from Utilities import Logger
from Utilities.ReadConfig import readConfigClass
from Utilities.ScreenShotsUtil import TakeScreenShoteUtil

logger = Logger.log_generator_class.loggen_method()


@pytest.mark.usefixtures("driver_setup")
class Test_Login_Class:
    driver = None
    login_url = readConfigClass.read_data_for_login_url()

    def test_login_config_read_T001(self):
        logger.info("inside test_login_config_read executing test case T001")
        self.driver.get(self.login_url)
        time.sleep(10)
        self.lp = Login_Page_class(self.driver)
        self.lp.enterusername(readConfigClass.read_data_username())
        self.lp.enterpassword(readConfigClass.read_data_password())
        time.sleep(4)
        self.lp.click_login_btn()
       # print(">>>>>>>>>>>>>>>>>>>> "+self.driver.title)
        if self.lp.verify_login() == 'pass':
            # path = TakeScreenShoteUtil.takeScreenShots(self.driver, "test_login_config_read_T001")
            #  allure.attach.file(path, name="User login Successfully", attachment_type=allure.attachment_type.PNG)
            # TakeScreenShoteUtil.takeScreenShots(self.driver, "test")
            scr_sts_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

            # path = "..\\ScreenShots\\testcase" + scr_sts_datetime + ".png"
            path = "D:/CRED_2025/CRE_2025/pythonProject2/ScreenShots/pass_test_login_config_read_T001" + scr_sts_datetime + ".png" + ""
            self.driver.save_screenshot(path)
            allure.attach.file(path, name="User login Successfully", attachment_type=allure.attachment_type.PNG)
            logger.info("inside test_login_config_read executing test case T001 pass")
            assert True

        else:
            # path = TakeScreenShoteUtil.takeScreenShots(self.driver, "test_login_config_read_T001")
            # allure.attach.file(path,name="User login Successfully", attachment_type=allure.attachment_type.PNG)
            scr_sts_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

            # path = "..\\ScreenShots\\testcase" + scr_sts_datetime + ".png"
            path = "D:/CRED_2025/CRE_2025/pythonProject2/ScreenShots/fail_test_login_config_read_T001" + scr_sts_datetime + ".png" + ""
            self.driver.save_screenshot(path)
            allure.attach.file(path, name="User login Successfully", attachment_type=allure.attachment_type.PNG)
            logger.info("inside test_login_config_read executing test case T001 fail")
            assert False




    def test_title_Check_T002(self):
        logger.info("executing test_title_Check_T002 ")
        title=self.driver.title


        if title=="OrangeHRM":
            scr_sts_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = "D:/CRED_2025/CRE_2025/pythonProject2/ScreenShots/pass_test_title_Check_T002" + scr_sts_datetime + ".png" + ""
            self.driver.save_screenshot(path)
            allure.attach.file(path, name="Title check Successfully", attachment_type=allure.attachment_type.PNG)
            logger.info("executing test_title_Check_T002 pass")
            assert True
        else:
            scr_sts_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = "D:/CRED_2025/CRE_2025/pythonProject2/ScreenShots/fail_test_title_Check_T002" + scr_sts_datetime + ".png" + ""
            self.driver.save_screenshot(path)
            allure.attach.file(path, name="Title check unsuccessfully", attachment_type=allure.attachment_type.PNG)
            logger.info("executing test_title_Check_T002 fail")
            assert False
