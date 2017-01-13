import yaml
import os
from readyaml import RY
from appium import webdriver
# from selenium import webdriver
# from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
# device = MonkeyRunner.waitForConnection()
# driver =  webdriver.Remote('https://localhost:4723/wd/hub',None)
# test_type 查找类型
# test_name 命令信息
# test_param 元素信息
# test_count 操作次数
# test_text 发送数据
# test_operate 操作类型
cases = RY().readcase('testcase.yaml')

find_type = {
    'by_id': lambda x: driver.find_element_by_id(x)
}
# print(cases)
for case in cases:
    # print(case['test_id'])
    # print(case['test_control'])
    print(case)
    if 'test_text' not in case.keys():
        print('hah')
# webview = driver.contexts[-1]
# driver.switch_to.context(webview)
