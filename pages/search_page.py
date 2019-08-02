#!usr/bin/env python

#-*- coding:utf-8 -*-

import os, sys

from selenium.webdriver.common.by import By
sys.path.append(os.getcwd())
from base.base_action import BaseAction

class SearchPage(BaseAction):
    # # 点击放大镜
    # self.search_page.click_serach()
    # # 输入文字
    # self.search_page.input_content()
    # # 点击返回
    # self.search_page.click_back()
    # 显示按钮 本质上是元组
    click_serach_button = By.ID, "com.android.settings:id/search"
    # 搜索按钮
    input_content_button = By.ID, "android:id/search_src_text"
    # 写入文本按钮
    click_back_button = By.XPATH, "//*[contains(@class,'android.widget.ImageButton')]"

    def click_serach(self):
        self.click(self.click_serach_button)

    def input_content(self, text):
        self.input_text(self.input_content_button, text)

    def click_back(self):
        self.click(self.click_back_button)