# # import yaml
# # try:
# #     with open('device.yaml', encoding='utf-8') as f:
# #         x = yaml.load(f)
# #         print(x)
# # except Exception as e:
# #     raise e
# # print(len(x['appium']))
# import os
# import subprocess

# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )
# # "E:\adt-bundle-windows-x86_64-20140702\sdk\build-tools\android-4.4W\aapt.exe"


# def get_apk_name(path=''):
#     command = 'E:\\adt-bundle-windows-x86_64-20140702\sdk\\build-tools\\android-4.4W\\aapt dump badging \"%s\" | grep versionName' % path
#     # command = 'aapt dump badging \"%s\" | grep versionName'
#     print(command)
#     # return subprocess.Popen(command, stdout=subprocess.PIPE,
#     # stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
#     return subprocess.check_output(command, shell=True)

# # print(get_apk_name("E:\\sub_extensions\\appium_auto_try\\gomeplus-meixin-release.apk").stdout.read().decode('utf-8'))
# # print(get_apk_name(
#     # 'E:\\sub_extensions\\appium_auto_try\\gomeplus-meixin-release.apk').communicate()[1].decode(	))
# (output, error) = get_apk_name(
#     'E:\\sub_extensions\\appium_auto_try\\gomeplus-meixin-release.apk')
# # if output != "":
# #     result = output.split()[0].decode()
# print(output)
# print(error.decode('gb2312'))

import subprocess

# p1 = subprocess.Popen(
#     ['E:\\adt-bundle-windows-x86_64-20140702\\sdk\\build-tools\\android-4.4W\\aapt dump badging E:\\sub_extensions\\appium_auto_try\\gomeplus-meixin-release.apk'], stdout=subprocess.PIPE)
p1 = subprocess.Popen(['E:\\adt-bundle-windows-x86_64-20140702\\sdk\\build-tools\\android-4.4W\\aapt', 'dump', 'badging',
                       'E:\\sub_extensions\\appium_auto_try\\gomeplus-meixin-release.apk'], stdout=subprocess.PIPE)
# print(p1.communicate()[0])
p2 = subprocess.Popen(['find', 'name'],
                      stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output, error = p2.communicate()
print(output)
print(error)
import os
print(os.popen('echo hello').read())
o = os.popen('adb -s ff31b441 shell pm list packages | findstr meixin')
print(o.read())
print(os.popen('adb devices'))
