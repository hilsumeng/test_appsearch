#!usr/bin/env python

#-*- coding:utf-8 -*-

#!usr/bin/env python

#-*- coding:utf-8 -*-

# 增加建所目录
import os, sys
sys.path.append(os.getcwd())

import pytest
from appium import webdriver
import time
from base import base_driver
from pages import network_page

class TestSetting:

    def setup(self):
        self.driver = base_driver.init_driver()
        self.network_page = network_page.NetworkPage(self.driver)

    def test_mobile_network_2g(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()
        self.network_page.click_more()
        time.sleep(1)
        self.network_page.click_mobile_network()
        self.network_page.click_first_network()
        self.network_page.select_2g_network()


    def test_mobile_network_3g(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()
        self.network_page.click_more()
        self.network_page.click_mobile_network()
        self.network_page.click_first_network()
        self.network_page.select_3g_network()
