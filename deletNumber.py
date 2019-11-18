from appium import webdriver
import time
import re
from oneApp import runfang


###通过阿松的删除通讯录软件，进行删除
def deleteNumber(geshu):
    ###连接删除软件，
    desired_caps = {'platformName': 'Android', 'platformVersion': '6.0', 'deviceName': '192.168.56.102:5555',
                    'appPackage': 'com.xiaomai.cliearmearlist', 'appActivity': '.MainActivity'}
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(1)
    driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
    time.sleep(1)
    driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
    time.sleep(2)
    driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view'
        '.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText').send_keys(
        geshu)
    time.sleep(2)
    driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Button[1]').click()
    time.sleep(2)
    # zi = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.TextView').text
    # print(zi)
    # if zi == '删除成功':
    #     print("删除成功，继续执行")

    print("删除完毕")



