from selenium import  webdriver
from .driver import browser
import unittest
from shareweb.test_case.models.getconfig import *
import os


class MyTest(unittest.TestCase):

    def setUp(self):
        browser_name = get_browser_name()
        browser_version = get_browser_version()
        self.driver = browser(browser_name, browser_version)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
