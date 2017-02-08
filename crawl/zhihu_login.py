import requests
from bs4 import BeautifulSoup
from PIL import Image
import time

#<input type="hidden" name="_xsrf" value="2cdc3f248d3edb22438e0f57bfc786ab"/>
# 第一次的时候就不用输入验证码，尽量避免输入验证码
# 实在不行的话，可以尝试使用Pillow的模块来解析简单的验证码

# _xsrf:46572bcb45716b6acbdb7b04d3dea747
# password:wyqzhihu
# captcha:p6rm
# email:wyqexpect@163.com


# 要考虑到cookie的问题，用session来做处理
# cur_session = requests.session

# 登录成功之后要做抓取工作的话就需要使用登录成功之后的cookie了
class login:

    def __init__(self):
        self.xsrf = ''
        self.login_url = 'https://www.zhihu.com/#signin'
        self.email_url = 'https://www.zhihu.com/login/email'
        self.cookies = ''
        self.headers = {}
        self.headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

    def get_captcha(self, cur_session, cur_headers):
        captcha_url = 'http://www.zhihu.com/captcha.gif?r=%s&type=login' % int(
            time.time() * 1000)
        r = cur_session.get(captcha_url, headers=cur_headers)
        with open('captcha.gif', 'wb') as f:
            f.write(r.content)
        im = Image.open('captcha.gif')
        im.show()
        im.close()
        captcha = input()
        return captcha

    def login(self, username, password):
        login_session = requests.session()
        r = login_session.get(self.login_url, headers=self.headers)
        print(r.status_code)
        self.xsrf = BeautifulSoup(r.content, 'html.parser').find(
            type='hidden').get('value')
        print(self.xsrf)
        if '@' in username:
            # return
            formdata = {
                '_xsrf': self.xsrf,
                'email': 'wyqexpect@163.com',
                'password': 'wyqzhihu',
                'captcha': self.get_captcha(login_session, self.headers)
                # 'remember_me': 'true'
            }
            r = login_session.post(self.email_url, data=formdata,
                                   headers=self.headers)
            if r.status_code == 200:
                print('login success')
            else:
                print('login error')
        else:
            print('num')
if __name__ == '__main__':
    # login().login('111@qq.com', 11)
    # 已经可以登录成功了，需要切换build系统
    pass
    # PIL会占用资源，其实是已经输入了的
    # im = Image.open('captcha.gif')
    # im.show()
    # i = input()
    # im.close()
    # print(i)