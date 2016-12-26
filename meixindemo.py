# coding=utf-8
#! /usr/bin/env python
import os
import time

from appium.webdriver.mobilecommand import MobileCommand
import unittest
from appium import webdriver
# from lib2to3.pgen2.driver import Driver
from selenium.webdriver.common.keys import Keys
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'Android'
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"
desired_caps['autowebview'] = "True"
desired_caps['appPackage'] = 'cn.com.gome.meixin'
desired_caps[
    'appActivity'] = 'cn.com.gome.meixin.ui.other.activity.LaunchActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
print(time.ctime())
time.sleep(15)
print(time.ctime())
# 进入消息
# driver.find_element_by_id("cn.com.gome.meixin:id/rbtn_im").click()
# time.sleep(5)
# #返回
# #driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# #进入逛逛
# driver.find_element_by_id("cn.com.gome.meixin:id/rbtn_meixin").click()
# time.sleep(5)
# #进入圈子
# driver.find_element_by_id("cn.com.gome.meixin:id/rbtn_imchat").click()
# time.sleep(5)
# 进入购物车
# driver.find_element_by_id("cn.com.gome.meixin:id/rbtn_meshop").click()
# time.sleep(5)
# 返回
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# time.sleep(5)
# 进入我的
driver.find_element_by_id("cn.com.gome.meixin:id/rbtn_commission").click()
# 进入登陆页面
"""
driver.find_element_by_id("cn.com.gome.meixin:id/iv_mine_head").click()
#点击用户名
driver.find_element_by_id("cn.com.gome.meixin:id/et_login_phone_num").click()
phone_num = driver.find_element_by_id("cn.com.gome.meixin:id/et_login_phone_num")
phone_num.send_keys('15757821913')
#点击密码
driver.find_element_by_id("cn.com.gome.meixin:id/et_login_password").click()
password= driver.find_element_by_id("cn.com.gome.meixin:id/et_login_password")
password.send_keys('gome1234567')
#点击验证码
driver.find_element_by_id("cn.com.gome.meixin:id/et_login_image_checked").click()
validy= driver.find_element_by_id("cn.com.gome.meixin:id/et_login_image_checked")
validy.send_keys(Keys.ENTER)
validy.send_keys('0000')
# driver.hide_keyboard()
#validy.send_keys(Keys.BACK_SPACE)
#点击登陆
driver.find_element_by_id("cn.com.gome.meixin:id/btn_login_complete").click()
"""
# 我的圈子
# driver.find_element_by_name("我的圈子").click()
# time.sleep(10)
# #返回
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# #我的话题
# driver.find_element_by_name("我的话题").click()
# time.sleep(7)
# #返回
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# #我的收藏
# driver.find_element_by_id("cn.com.gome.meixin:id/rl_mine_collect").click()
# time.sleep(7)
# #返回
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# #电影订单
# driver.find_element_by_id("cn.com.gome.meixin:id/rl_mine_movie_order").click()
# time.sleep(7)
# #返回
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# #我要晒单
# driver.find_element_by_id("cn.com.gome.meixin:id/rl_mine_show").click()
# time.sleep(7)
# #返回
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# #邀请商家
# driver.find_element_by_id("cn.com.gome.meixin:id/rl_mine_invate_merchants").click()
# time.sleep(7)
# #返回
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# #意见反馈
# driver.find_element_by_id("cn.com.gome.meixin:id/textView5").click()
# time.sleep(7)
# #返回
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# #国美币
# driver.find_element_by_id("cn.com.gome.meixin:id/rl_mine_gome_money").click()
# time.sleep(5)
# #返回
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# #优惠券
# driver.find_element_by_id("cn.com.gome.meixin:id/rl_mine_tickets").click()
# time.sleep(5)
# #返回
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# #银行卡
# driver.find_element_by_id("cn.com.gome.meixin:id/rl_mine_withdraw").click()
# time.sleep(5)
# #取消
# driver.find_element_by_id("cn.com.gome.meixin:id/tv_dialog_cancle").click()
# time.sleep(5)
# #去设置
# #driver.find_element_by_id("cn.com.gome.meixin:id/tv_dialog_conform").click()
# #time.sleep(5)
# #返回
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# #返利
# driver.find_element_by_id("cn.com.gome.meixin:id/rl_mine_rebate").click()
# time.sleep(5)
# #返回
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# #我的账户
# driver.find_element_by_name("我的账户").click()
# time.sleep(5)
# #返回
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# #待付款
# driver.find_element_by_id("cn.com.gome.meixin:id/rl_mine_order_one").click()
# time.sleep(5)
# #返回
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# #待发货
# driver.find_element_by_id("cn.com.gome.meixin:id/rl_mine_order_two").click()
# time.sleep(5)
# #返回
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# #待收货
# driver.find_element_by_id("cn.com.gome.meixin:id/rl_mine_order_three").click()
# time.sleep(5)
# #返回
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# #待评价
# driver.find_element_by_id("cn.com.gome.meixin:id/rl_mine_order_four").click()
# time.sleep(5)
# #返回
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# #退款/售后
# driver.find_element_by_id("cn.com.gome.meixin:id/rl_mine_order_five").click()
# time.sleep(5)
# #返回
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# 进入店
driver.find_element_by_name("我的店铺").click()
time.sleep(10)
print(driver.contexts)
# driver.switch_to.context('WEBVIEW_cn.com.gome.meixin')
time.sleep(3)
#driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name":"WEBVIEW_cn.com.gome.meixin"})
# driver.switch_to.context{'name':'WEBVIEW_cn.com.gome.meixin'}
driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {
               'name': 'WEBVIEW_cn.com.gome.meixin'})
# driver.switch_to.context("WEBVIEW_cn.com.gome.meixin")
# print driver.page_source
# 商品管理
driver.find_element_by_id("productManageBtn").click()
time.sleep(5)
# 返回
# driver.find_element_by_xpath("android.widget.FrameLayout/android.webkit.WebView/android.view.View[3]/android.view.View[0]")
# driver.find_elements_by_class_name("android.widget.ImageButton")[0].click()
# driver.close()
# driver.implicitly_wait(9)
# driver.implicitly_wait