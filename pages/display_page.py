#!usr/bin/env python

#-*- coding:utf-8 -*-
# 抽取特征需要导入模块
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class DisplayPage(BaseAction):

    # 显示按钮 本质上是元组
    display_button = By.XPATH, "//*[contains(@text,'显示')]"
    # 搜索按钮
    search_button = By.ID, "com.android.settings:id/search"
    # 写入文本按钮
    input_text_button = By.ID, "android:id/search_src_text"
    # 返回键按钮
    click_back_button = By.XPATH, "//*[contains(@class,'android.widget.ImageButton')]"

    def __init__(self, driver):
        # 需要调用一下父类的__init
        BaseAction.__init__(self, driver)
        self.driver = driver

    def click_display(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # 直接调用driver中find_element方法
        # self.driver.find_element(By.XPATH, "//*[contains(@text,'显示')]")
        # 在page脚本中自己定义一个find_element方法 相当于抽取特征
        # self.find_element(self.display_button).click()
        # click()还可以抽取action 进行简化
        self.click(self.display_button)

    def click_search(self):
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.find_element(self.search_button).click()
        self.click(self.search_button)

    def input_search_text(self, text):
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys(text)
        # self.find_element(self.input_text_button).send_keys(text)
        self.input_text(self.input_text_button, text)



    def click_back(self):
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        # self.find_element(self.click_back_button).click()
        self.click(self.click_back_button)


    # 因为原来的driver.find_element需要传2个参数，但是定义的按钮只是一个元组
    # 所以定义一个叫find_element的新方法来接收按钮 然后再调用driver的方法
    # def find_element(self, loc):
    #     return self.driver.find_element(loc[0], loc[1])