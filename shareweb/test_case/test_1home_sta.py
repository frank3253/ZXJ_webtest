# -*- coding: utf-8 -*-
from shareweb.test_case.page_obj.home_page import Home
from selenium import webdriver
import unittest, random, sys
from time import sleep
from shareweb.test_case.models import myunit, function
import configparser


class HomeTestCast(myunit.MyTest):
    """测试PC首页"""

    cf = configparser.ConfigParser()
    path = "E:/ZXJ_webtest/config/config.ini"
    cf.read(path)
    cf.sections()

    ture_title = cf.get("testdata", "headertitle")

    def test_1_header_title(self):
        # 测试演讲标题是否正确
        po = Home(self.driver)
        po.open()
        sleep(5)
        ture_title = self.cf.get("testdata", "headertitle")
        header_title = po.get_header_title().text
        self.assertEqual(header_title, ture_title, msg=" headertitle is wrong ")
        function.insert_img(self.driver, "1_header_title.jpg")

    def test_2_page_number(self):
        # 测试页码
        po = Home(self.driver)
        po.open()
        sleep(5)
        page_number = po.get_page_number().text.split("/")[1]
        true_page_number = self.cf.get("testdata", "pagenumber")
        self.assertEqual(page_number, true_page_number, msg="the page number is wrong")
        function.insert_img(self.driver, "2_page_number.jpg")


if __name__ == '__main__':
    unittest.main()
