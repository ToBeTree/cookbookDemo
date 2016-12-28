import yaml
import os


class RY:
    def __init__(self):
        pass

    def readcase(self, path=''):
        case = yaml.load(open('testcase.yaml', 'r',encoding='utf-8'))
        print(case)
if __name__ == '__main__':
    ry = RY()
    ry.readcase()
