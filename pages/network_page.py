#!usr/bin/env python

#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class NetworkPage(BaseAction):

    # 更多按钮
    more_button = By.XPATH, "//*[contains(@text,'更多')]"
    # 移动网络按钮
    mobile_network_button = By.XPATH, "//*[contains(@text,'移动网络')]"
    # 首选网络按钮
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    # 2G网络按钮
    network_2g_button = By.XPATH, "//*[contains(@text,'2G')]"
    # 3G网络按钮
    network_3g_button = By.XPATH, "//*[contains(@text,'3G')]"

    # 因为没有改写父类方法 所以会自动调用父类的__init__方法 所以下面可以注释掉
    # def __init__(self, driver):
    #     BaseAction.__init__(self, driver)
    #     self.driver = driver


    def click_more(self):
        # self.find_element(self.more_button).click()
        self.click(self.more_button)


    def click_mobile_network(self):
        # self.find_element(self.mobile_network_button).click()
        self.click(self.mobile_network_button)

    def click_first_network(self):
        # self.find_element(self.first_network_button).click()
        self.click(self.first_network_button)

    def select_2g_network(self):
        # self.find_element(self.network_2g_button).click()
        self.click(self.network_2g_button)

    def select_3g_network(self):
        # self.find_element(self.network_3g_button).click()
        self.click(self.network_3g_button)

    # 因为原来的driver.find_element需要传2个参数，但是定义的按钮只是一个元组
    # 所以定义一个叫find_element的新方法来接收按钮 然后再调用driver的方法
    # def find_element(self, loc):
    #     return self.driver.find_element(loc[0], loc[1])
