#!usr/bin/env python

#-*- coding:utf-8 -*-

import os, sys

import pytest

sys.path.append(os.getcwd())
from base import base_driver
from pages.search_page import SearchPage
from base.base_yml import yml_data_with_file

def data_with_key(key):
    return yml_data_with_file("search_data")[key]

class TestSearch:

    def setup(self):
        self.driver = base_driver.init_driver()
        self.search_page = SearchPage(self.driver)

    @pytest.mark.parametrize("text", data_with_key("test_search"))
    def test_search(self,text):
        # 点击放大镜
        self.search_page.click_serach()
        # 输入文字
        self.search_page.input_content(text)
        # 点击返回
        self.search_page.click_back()

    @pytest.mark.parametrize("text", data_with_key("test_search1"))
    def test_search(self,text):
        # 点击放大镜
        self.search_page.click_serach()
        # 输入文字
        self.search_page.input_content(text)
        # 点击返回
        self.search_page.click_back()

