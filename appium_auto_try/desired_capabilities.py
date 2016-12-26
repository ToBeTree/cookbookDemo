import os

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

print(11)


def get_desired_capabilities(app):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '6.1',
        'deviceName': 'Android',
        'app': PATH('../appium_auto_try/' + app),
        'newCommandTimeout': 240
    }
    print(desired_caps['app'])
    return desired_caps
