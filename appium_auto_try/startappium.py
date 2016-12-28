import os
import random
import subprocess


class StartAppium:
    def __init__(self, device_id=''):
        self.device_id = device_id
        self.appium = ''

    def _start(self, port='4723', bport='4724'):
        command = 'appium -p %s -bp %s -U %s' % (port, bport, self.device_id)
        print(command)
        self.appium = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        self.appium.wait()
        # while True:
        #     print(self.appium.stdout.readline().decode('utf-8'))
        # print(self.appium.stdout.read().decode('utf-8'))

    def stop_appium(self):
        return self.appium.poll()

    def start(self):
        p = random.randint(4720, 9999)
        bp = random.randint(4720, 9999)
        self._start(p, bp)
        return p
if __name__ == '__main__':
    sa = StartAppium('ff31b441')
    print(sa.start())
    # print(sa.stop_appium())
