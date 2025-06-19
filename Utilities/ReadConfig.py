import configparser
import logging

from Utilities import Logger
import os

thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder,'..\\Configuration\\config.ini')
config = configparser.RawConfigParser()
res = config.read(initfile)
#config = configparser.RawConfigParser()
#config.read(r"..\Configuration\config.ini")
logger = Logger.log_generator_class.loggen_method()


class readConfigClass:

    @staticmethod
    def read_data_for_login_url():
        hrm_login_url = config.get("application url", "orange_hrm_login_url")
        logger.info("reading url data from config file ")
        return hrm_login_url

    @staticmethod
    def read_data_username():
        username = config.get("login-data", "username")
        logger.info("reading username data from config file ")
        return username

    @staticmethod
    def read_data_password():
        password = config.get("login-data", "password")
        logger.info("reading password data from config file ")
        return password




print(readConfigClass.read_data_username())
print(readConfigClass.read_data_password())