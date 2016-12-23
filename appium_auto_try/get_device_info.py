# -*- coding:utf-8
import os
import yaml
import subprocess


def cmd(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # return subprocess.getoutput(cmd).

# print(cmd('adb devices').stdout.readlines())
android_device_list = []
for device in cmd('adb devices').stdout.readlines():
    device = device.decode('utf-8')  # solve subproess return byte not str
    if 'device' in device and 'devices' not in device:
        device = device.split('\t')[0]
        android_device_list.append(device)

# for i in android_device_list:
#     print(i)


def set_device_yaml(devices):
    device_list = []
    for device in devices:
        cmd = 'adb -s %s shell getprop ro.build.version.release' % device
        print(cmd)
        device_list.append(
            {'platfromVersion': subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout.read().strip().decode('utf-8'), 'deviceName': device})

    # print(device_list)
    with open('device.yaml', 'w') as f:
        yaml.dump(device_list, f)

set_device_yaml(android_device_list)


def get_device_id():
    with open('device.yaml', 'r') as f:
        device_id_list = yaml.load(f)
    # print(device_id_list)
    return device_id_list[0]['deviceName']
# print(get_device_id())

if __name__ == '__main__':
    pass
