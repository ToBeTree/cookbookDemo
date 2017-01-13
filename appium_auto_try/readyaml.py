import yaml
import os


class RY:
    def __init__(self):
        pass

    def readcase(self, path=''):
        case_list = []
        cases = yaml.load(open(path, 'r', encoding='utf-8'))
        for case in cases:
            # print(type(case))
            # print(case)
            if 'test_inherit' in case.keys():
                for inherit in case.get('test_inherit'):
                    print('address: %s' % inherit)
                    case_list += self.readcase(inherit)
            else:
                case_list.append(case)
            # case_list = case_list + case
        # print(type(case))
        # print(case)
        return case_list
if __name__ == '__main__':
    ry = RY()
    cases = ry.readcase('testcase.yaml')
    print(len(cases))
    print('--------------')
    print(cases)

    # print(cases[0]['test_name'])
    # print(type(cases))
    # for case in cases:
    #     print(case.keys())
    # print(case.keys())
    # print(case.get('test_inherit'))
