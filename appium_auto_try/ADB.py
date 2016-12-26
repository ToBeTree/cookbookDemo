import subprocess

app_path = 'E:\\sub_extensions\\appium_auto_try\\gomeplus-meixin-release.apk'
package_name = 'cn.com.gome.meixin'


class ADB:
    def __init__(self, device_id=''):
        if device_id == '':
            self.device_id = device_id
        else:
            self.device_id = '-s %s' % device_id

    def adb(self, command=''):
        command = 'adb %s' % command
        print(command)
        return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def shell(self, command=''):
        command = 'adb %s shell %s' % (self.device_id, command)
        print(command)
        return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def __cformat__(self, func):
        return func.stdout.read().strip().decode('utf-8')

    def get_device_version(self):
        command = 'getprop ro.build.version.release'
        return self.__cformat__(self.shell(command))

    def get_device_model(self):
        command = 'getprop ro.product.model'
        return self.__cformat__(self.shell(command))

    def clear_cache(self, package_name=''):
        command = 'pm clear %s' % package_name
        return 'clear cache %s' % self.__cformat__(self.shell(command))

    def install_app(self, app_path=''):
        command = 'install %s' % app_path
        if 'Success' in self.__cformat__(self.adb(command)):
            return '%s install Success' % package_name
        return '%s install Fail' % package_name

    def remove_app(self, package_name=''):
        command = 'uninstall %s' % package_name
        if 'Success' in self.__cformat__(self.adb(command)):
            return '%s uninstall Success' % package_name
        return '%s uninstall error, please check' % package_name

    def is_app_installed(self, package_name=''):
        command = 'pm list packages %s ' % package_name
        if package_name in self.__cformat__(self.shell(command)):
            print('%s is already installed' % package_name)
            return True
        print('%s not installed, please intall' % package_name)
        return False
if __name__ == '__main__':
    a = ADB('ff31b441')
    # print(a.get_device_version())
    # print(a.get_device_model())
    # a.is_app_installed(package_name)
    # print(a.remove_app(package_name))
    # print(a.install_app(app_path))
    # print(a.clear_cache(package_name))
