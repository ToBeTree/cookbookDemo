import unittest
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Remote()
driver.keyevent()
driver.implicitly_wait()
from selenium.webdriver.support.ui import WebDriverWait
# 按下home键吗？隐藏？
driver.background_app
driver.is_app_installed
driver.install_app
driver.remove_app
driver.close_app
driver.launch_app
driver.end_test_coverage
driver.set_network_connection
driver.network_connection
driver.switch_to_alert()
import
from appium import on_platforms, SauceTestCase
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
import datetime
# zhuang shi qi
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(classname)
    unittest.TextTestRunner(verbosity=2).run(suite)
