import configparser
import os
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class CP:
    def __init__(self):
        self.cp = configparser.ConfigParser()
        self.cp.read('TestConfig.ini')

    def get_ini(self, title='', key=''):
        return self.cp.get(title, key)

    def set_ini(self, title='', key='', value=''):
        self.cp.set(title, key, value)
        return self.cp.write(open('TestConfig.ini', 'w+'))

    def add_ini(self, title=''):
        self.cp.add_section(title)
        return self.cp.write(open('TestConfig.ini'))

    def get_options(self,title=''):
        return self.cp.options(title)


if __name__ == '__main__':
    cp = CP()
    print(cp.get_ini('test_package_name', 'package_name'))
    print(cp.get_options('test_package_name'))
    print(cp.set_ini('test_package_name','test_activity','com.example'))