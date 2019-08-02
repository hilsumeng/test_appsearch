#!usr/bin/env python

#-*- coding:utf-8 -*-
import allure
import allure_pytest




class TestContact:
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("ssss")
    def test_login1(self):
        allure.attach("123","测试123")
        print("123")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step(title="登录测试脚本2")
    def test_login2(self):
        print("123")

    # MINOR
    @allure.severity(allure.severity_level.MINOR)
    @allure.step(title="登录测试脚本3")
    def test_login3(self):
        print("123")