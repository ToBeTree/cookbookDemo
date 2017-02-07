import requests
from bs4 import BeautifulSoup

#<input type="hidden" name="_xsrf" value="2cdc3f248d3edb22438e0f57bfc786ab"/>
# 第一次的时候就不用输入验证码，尽量避免输入验证码
# 实在不行的话，可以尝试使用Pillow的模块来解析简单的验证码

class login:
    def __init__(self):
        self.xsrf = ''
        self.url = 'https://www.zhihu.com/#signin'
        self.emailurl = 'https://www.zhihu.com/login/email'
        self.cookies = ''
        self.headers = {}
        self.headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

    def login(self, username, password):
        r = requests.get(self.url, headers=self.headers)
        self.cookies = r.cookies
        self.xsrf = BeautifulSoup(r.content, 'html.parser').find(
            type='hidden').get('value')
        if '@' in username:
            formdata = {
                '_xsrf': self.xsrf,
                'email': 'wyqexpect@163.com',
                'password': 'wyqzhihu',
                'remember_me': 'true'
            }
            r = requests.post(self.emailurl, json=formdata,
                              cookies=self.cookies)
            if r.status_code == 200:
                print('login success')
            else:
                print('login error')
        else:
            print('num')
        print(self.xsrf)
if __name__ == '__main__':
    login().login('111@qq.com', 11)
