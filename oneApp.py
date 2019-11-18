from appium import webdriver
import time
import xlwt
import re
from selenium.common.exceptions import StaleElementReferenceException
import deletNumber
import random
import sys
import os

QUANJU = 0
##通讯录按钮的xpath
tong = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget' \
       '.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget' \
       '.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget' \
       '.LinearLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout' \
       '/android.widget.FrameLayout[5]/android.widget.TextView '
##前往开启通讯录按钮
gotong = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget' \
         '.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget' \
         '.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget' \
         '.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout' \
         '/android.widget.AbsListView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button '
##点击允许开启通讯录按钮
yunxu = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget' \
        '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2] '


def getAppium():
    global driver
    desired_caps = {'platformName': 'Android', 'platformVersion': '6.0', 'deviceName': '192.168.56.102:5555',
                    'appPackage': 'com.tencent.mobileqq', 'appActivity': '.activity.SplashActivity', 'noReset': True}
    time.sleep(1)
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# 滑动方法
def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


# 实现滑动
def huadong(t=1000, n=1):
    time.sleep(0.5)
    try:
        l = get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.45)
        y2 = int(l[1] * 0.25)
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)
    except:
        print("重新其运行1")
        return


# 实现滑动2
def huadong2(t=1000, n=1):
    try:
        l = get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.84)
        y2 = int(l[1] * 0.25)
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)
    except:
        print("重新其运行2")
        runfang()


def Left(t=500, n=1):
    try:
        l = get_size()
        x1 = int(l[0] * 0.8)
        y1 = int(l[0] * 0.2)
        y2 = int(l[1] * 0.5)
        for i in range(n):
            driver.swipe(x1, y2, y1, y2, t)
    except:
        print("重新其运行3")
        Left()


# 实现下拉刷新
def xiala(t=500, n=1):
    try:
        l = get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)
    except:
        print("重新其运行4")
        xiala()


# 获取元素
def get_element(tj, G_element):
    try:
        time.sleep(0.5)
        if tj == 'id':
            return driver.find_element_by_id(G_element)
        elif tj == 'xpath':
            return driver.find_element_by_xpath(G_element)
        elif tj == 'class':
            return driver.find_element_by_class_name(G_element)
    except:
        print("并未找到元素11")
        time.sleep(0.5)


# 获取元素集合
def get_elements(tj, G_element):
    try:
        time.sleep(0.5)
        if tj == 'id':
            return driver.find_elements_by_id(G_element)
        elif tj == 'xpath':
            return driver.find_elements_by_xpath(G_element)
        elif tj == 'class':
            return driver.find_elements_by_class_name(G_element)
    except:
        print("并未找到元素222")
        time.sleep(1)
        runfang()


# 判断一个元素存不存在
def is_element(identifyBy, elment):
    time.sleep(1)
    flag = None
    try:
        if identifyBy == "id":
            driver.find_element_by_id(elment)
        elif identifyBy == "xpath":
            driver.find_element_by_xpath(elment)
        elif identifyBy == "class":
            driver.find_element_by_class_name(elment)
        elif identifyBy == "link text":
            driver.find_element_by_link_text(elment)
        elif identifyBy == "partial link text":
            driver.find_element_by_partial_link_text(elment)
        elif identifyBy == "name":
            driver.find_element_by_name(elment)
        elif identifyBy == "tag name":
            driver.find_element_by_tag_name(elment)
        elif identifyBy == "css selector":
            driver.find_element_by_css_selector(elment)
        flag = True
    except:
        flag = False
    finally:
        return flag


# 点击元素方法
def click_element(fangshi, C_element):
    try:
        time.sleep(0.5)
        if fangshi == 'id':
            driver.find_element_by_id(C_element).click()
        elif fangshi == 'xpath':
            driver.find_element_by_xpath(C_element).click()
        elif fangshi == 'class':
            driver.find_element_by_class_name(C_element).click()
    except:
        print("并未找到元素4444")
        time.sleep(1)
        print("更换qq")
        changeNumber()
        print("从新运行方法")
        runfang()


##首页输入框元素
get_iielement = '738abbfe-6043-4a41-94ca-ad986d6d8561'
##联系人按钮元素
get_liaxi_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout' \
                  '/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget' \
                  '.FrameLayout/android.widget.TabWidget/android.widget.FrameLayout[1] '
##单个联系人元素
get_people_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout' \
                   '/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget' \
                   '.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup' \
                   '/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android' \
                   '.widget.FrameLayout/android.widget.LinearLayout/android.widget.AbsListView/android.widget' \
                   '.RelativeLayout[1] '
##通讯录按钮元素
get_Txl_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android' \
                '.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout' \
                '/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget' \
                '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget' \
                '.HorizontalScrollView/android.widget.LinearLayout/android.widget.FrameLayout[' \
                '5]/android.widget.TextView '
##联系人列表元素
get_Plist_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout' \
                  '/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget' \
                  '.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android' \
                  '.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget' \
                  '.FrameLayout/android.widget.LinearLayout/android.widget.AbsListView '
##返回按钮
get_fh_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android' \
             '.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[' \
             '1]/android.widget.RelativeLayout/android.widget.TextView[2] '
text1, text3, text4 = '', '', ''


## 如果获取元素失败，报错，重新获取循环三遍，
def get_yuansu(QUANJU=0):
    try:
        text1 = get_elements('class', 'android.widget.TextView')[2].text
        time.sleep(0.5)
        text3 = get_elements('class', 'android.widget.TextView')[3].text
        time.sleep(0.2)
        text4 = get_elements('class', 'android.widget.TextView')[0].text
        # print(text1, text3, text4)
        return text1, text3, text4

    except StaleElementReferenceException:
        print("报错")
        QUANJU += 1
        print(QUANJU)
        for i in range(3):
            get_yuansu()


def changeNumber():
    getAppium()
    click_element('xpath',
                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                  '/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget'
                  '.FrameLayout/android.widget.RelativeLayout')
    click_element('xpath',
                  '//android.widget.Button[@content-desc="设置"]/android.widget.RelativeLayout/android.widget.ImageView')
    click_element('id', 'com.tencent.mobileqq:id/account_switch')
    time.sleep(0.5)
    click_element(
        'xpath',
        '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android'
        '.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout'
        '/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]')
    time.sleep(0.5)
    click_element('id', 'com.tencent.mobileqq:id/ivTitleBtnLeft')
    click_element('xpath',
                  '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout'
                  '/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android'
                  '.widget.TextView[1]')
    Left(n=1)
    ####导入下一组手机号，  刷新界面，等待4秒

    print("执行完毕")
    print("重新启动run方法")
    runfang()


def ranstr(num):
    # 猜猜变量名为啥叫 H
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    salt = ''
    for i in range(num):
        salt += random.choice(H)
    return salt


kong = 0

stus1 = ''


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


## 判断一个元素存不存在 ，使用is_element方法来判断，需要传入查找方式和元素值
def runfang():
    time.sleep(1)
    getAppium()
    time.sleep(2)
    global num
    global stus1
    num = 1
    book = xlwt.Workbook()
    stus = [
        ['性别', '年龄', '地区', '编号', '手机号'],
    ]
    sheet = book.add_sheet('sheet1')
    print(num)
    if num == 2:
        changeNumber()
    if is_element(id, get_iielement):
        print("元素存在，点击联系人按钮")
        click_element('xpath', get_liaxi_xpath)
        if is_element('xpath', get_people_xpath):
            # 执行操作
            print('《《直接进行获取')
        else:
            time.sleep(0.5)
            click_element('xpath', get_Txl_xpath)
            conunt = 1
            count_range = 3000
            bianshu = 1
            print("下拉操作")
            xiala(n=1)
            time.sleep(1)
            for bianshu in range(count_range):
                bianshu += 1
                time.sleep(1)
                print("这是第" + str(bianshu) + "遍")
                number = 1
                if conunt == 9:
                    huadong2(n=1)
                    time.sleep(2)
                    conunt = conunt * 0 + 1
                time.sleep(1)
                ##判断是不是第一次进来
                PD_new_friend = is_element('xpath', '//android.widget.RelativeLayout[@content-desc="新朋友 按钮"]')
                if PD_new_friend:
                    print("判断成功")
                    try:
                        huadong(n=1)
                    except:
                        huadong(n=1)
                zhuan = str(conunt)
                ii = get_element('xpath',
                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                 ".FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget"
                                 ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                 ".LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
                                 ".LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android"
                                 ".widget.LinearLayout/android.widget.AbsListView/android.widget.RelativeLayout[" +
                                 zhuan + "]")
                time.sleep(2)
                try:
                    ii.click()
                except:
                    restart_program()
                conunt = conunt + 1
                time.sleep(1)
                ###调用获取元素函数
                try:
                    text1, text3, text4 = get_yuansu()
                except:
                    text1, text3, text4 = get_yuansu()
                list_text = re.split(' ', text1)
                # 个人资料的长度
                GRZL = len(list_text)
                if GRZL != 1 | GRZL != 3:
                    if GRZL != 4:
                        # print(text1)
                        print(">>>>>>>>>>")
                        list_four_Five = list_text[4] + list_text[5]
                        stus = stus + [[list_text[0], list_text[2], list_four_Five, text4, text3]]
                        stus1 = stus1 + ',' + text4
                elif GRZL == 3:
                    stus = stus + [[list_text[0], list_text[2], '无', text4, text3]]
                    stus1 = stus1 + ',' + text4
                    print(list_text[0], list_text[2], text4)
                elif GRZL == 4:
                    list_four_Three = list_text[1] + list_text[2]
                    stus1 = stus1 + ',' + text4
                    stus = stus + [[list_text[0], '无', '无', text4, list_four_Three]]
                    print(list_text[0], text4)
                else:
                    GSHU = len(list_text[0])
                    if GSHU == 1:
                        stus = stus + [[list_text[0], '无', '无', text4, '无']]
                        print(list_text[0], text4)
                    stus1 = stus1 + ',' + text4
                changdu = get_elements('class', 'android.widget.LinearLayout')
                print(stus)
                global kong
                print(stus1)
                cunzai = text4 in stus1
                print(cunzai)
                if len(changdu) <= 15:
                    kong += 1
                    print(kong)
                elif len(changdu) >= 16:
                    kong *= 0
                    print(kong)
                Lxl = 0
                if kong == 7:
                    if Lxl == 0:
                        pass
                    #判断是不是第一次进来。如果是第一次，向函数中传入bianshu 变量值，如果是第二次进来在原来的bianshu加上当前的bianshu
                    #就等于应该向第几行添加
                    Lxl += 1
                    line = 0  # 控制的是行
                    for stu in stus:
                        col = 0
                        for s in stu:
                            sheet.write(line, col, s)
                            col += 1
                        line += 1
                    suiji = ranstr(5)
                    book.save(suiji + '.xls')
                    print("账号已被限制，保存到excel数据")
                    print(kong)
                    print("删除相应的个数" + str(bianshu))
                    ##切换qq号操作
                    time.sleep(1)
                    print("切换qq号")
                    changeNumber()
                    print("删除通讯录")
                    deletNumber.deleteNumber(stus1)
                    kong = kong * 0
                    time.sleep(2)
                    runfang()
                ###分割
                # 写excel
                print("跳出来了")
                click_element('xpath', get_fh_btn)
            print(bianshu)
            print(count_range)
        line = 0  # 控制的是行
        for stu in stus:
            col = 0
            for s in stu:
                sheet.write(line, col, s)
                col += 1
            line += 1
        suiji = ranstr(5)
        book.save(suiji + '.xls')
    else:
        if is_element('xpath', get_people_xpath):
            # 执行操作
            print('直接进行获取')
        else:
            click_element('xpath', get_Txl_xpath)
            # 执行操作
            print("没有进入通讯录")


def runFangfa():
    for i in range(100):
        runfang()


if __name__ == '__main__':
    runfang()
