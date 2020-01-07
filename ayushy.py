# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Ayush(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/Users/tamerjar/Desktop/chromedriver2")
        self.driver.implicitly_wait(30)
        self.verificationErrors = []

    def test_ayush(self):
        driver = self.driver
        driver.get("http://dec.vumk.eu/student/web/site/login")
        driver.find_element_by_id("UserLoginForm_username").click()
        driver.find_element_by_id("UserLoginForm_username").clear()
        driver.find_element_by_id("UserLoginForm_username").send_keys("tamerjar")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Remember me'])[1]/following::center[1]").click()
        driver.find_element_by_id("UserLoginForm_password").click()
        driver.find_element_by_id("UserLoginForm_password").clear()
        driver.find_element_by_id("UserLoginForm_password").send_keys("Tamer710")
        driver.find_element_by_id("login-content-button").click()
        time.sleep(10)



    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
