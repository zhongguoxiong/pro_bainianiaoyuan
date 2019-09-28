import allure
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
class TestHome:
    # 登录成功测试场景

    def test_login_success(self):
        desired_caps = dict()
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "5.1"
        desired_caps["noReset"] = True
        # desired_caps['automationName'] = 'Uiautomator2'

        desired_caps["deviceName"] = "192.168.138.103:5555"  # 真机测试的时候必须写
        desired_caps["appPackage"] = "com.yunmall.lc"
        desired_caps["appActivity"] = "com.yunmall.ymctoc.ui.activity.MainActivity"
        desired_caps["unicodeKeyboard"] = True  # 表示开启unicode键盘
        desired_caps["resetKeyboard"] = True  # 重置当前键盘

        # 3 建立连接 获取driver对象
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        ele_me = (By.ID, "com.yunmall.lc:id/tab_me")
        obj_me = WebDriverWait(driver, 5000, 0.5).until(lambda x: x.find_element(*ele_me))
        obj_me.click()