import yaml
import os


class RY:
    def __init__(self):
        pass

    def readcase(self, path=''):
        case = yaml.load(open('testcase.yaml', 'r', encoding='utf-8'))
        # print(type(case))
        print(case)
        return case
if __name__ == '__main__':
    ry = RY()
    cases = ry.readcase()
    # print(type(cases))
    for case in cases:
        print(case.get('test_inherit', False))
