import os
import subprocess
import get_device_info

app_path = 'E:\\sub_extensions\\appium_auto_try\\gomeplus-meixin-release.apk'
package_name = 'cn.com.gome.meixin'


def is_install(package_name=''):
    cmd = 'adb shell pm list packages {}'.format(package_name)
    data = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    # data = data.stdout.read().decode('utf-8')
    if package_name in data.stdout.read().decode('utf-8'):
        return True
    return False


def remove_app(package_name=''):
    if is_install(package_name):
        cmd = 'adb uninstall {}'.format(package_name)
        data = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        if b'Success' in data.stdout.read():
            print('Success uninstall app')
            return True
        else:
            print('Failed uninstall app')
    else:
        print('app not installed')
    return False


def install_app(app_path=''):
    print('installing app....')
    cmd = 'adb -s {} install -r {}'.format(
        get_device_info.get_device_id(), app_path)
    data = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    if b'Success' in data.stdout.read():
        print('app install Success')
    else:
        print('app install Failed')

if is_install(package_name):
    print('app already installed')
    print('ready uninstall app...')
    if remove_app(package_name):
        print('app is uninstalled')
    else:
        print('app uninstall fail')
else:
    print('app not install')
    print('ready install app')
    install_app(app_path)

# if __name__ == '__main__':
#     pass
