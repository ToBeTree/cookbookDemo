from appium import webdriver
import desired_capabilities
from selenium.common.exceptions import WebDriverException
# import yaml

# with open('testcase.yaml', 'r', encoding='utf-8') as f:
#     a = yaml.load(f)

# for b in a:
#     print(b)
#     print()
try:
    driver = webdriver.Remote('http://127.0.0.1:8366/wd/hub',
                              desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk'))
    print(driver.close_app())
    driver.close_app()
    driver.quit()
except WebDriverException:
    print('a session already in process')
    # driver.quit()
# driver.shake()

# e = driver.find_element_by_id()
# e.click()
# e.send_keys
# e.swipe
