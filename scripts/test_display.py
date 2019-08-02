#!usr/bin/env python

#-*- coding:utf-8 -*-


# 增加检索目录
import os, sys
sys.path.append(os.getcwd())

import pytest
from appium import webdriver
from base import base_driver
from pages import display_page

class TestSetting:

    def setup(self):
        self.driver = base_driver.init_driver()
        self.display_page = display_page.DisplayPage(self.driver)

    def test_mobile_display_input(self):
        # 点击显示
        self.display_page.click_display()
        # 点击放大镜
        self.display_page.click_search()
        # 输入文字
        self.display_page.input_text("hello")
        # 点击返回
        self.display_page.click_back()

        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()