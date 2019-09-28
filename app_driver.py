from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
desired_caps = dict()

# 2 添加数据
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "5.1"
desired_caps["noReset"] = True
#desired_caps['automationName'] = 'Uiautomator2'

desired_caps["deviceName"] = "192.168.138.103:5555"  # 真机测试的时候必须写
desired_caps["appPackage"] = "com.yunmall.lc"
desired_caps["appActivity"] = "com.yunmall.ymctoc.ui.activity.MainActivity"
desired_caps["unicodeKeyboard"] = True  # 表示开启unicode键盘
desired_caps["resetKeyboard"] = True  # 重置当前键盘

# 3 建立连接 获取driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

ele_me=(By.ID,"com.yunmall.lc:id/tab_me")
obj_me=WebDriverWait(driver, 10000, 0.5).until(lambda x: x.find_element(*ele_me))
obj_me.click()
#size_dict=driver.get_window_size()
# w=1300
# h=2200
# w=size_dict["width"]
# h=size_dict["height"]

# start_x=w*0.5
# start_y=h*0.8
# end_x=w*0.5
# end_y=h*0.2
# driver.swipe(start_x,start_y,end_x,end_y)