import requests
from bs4 import BeautifulSoup
import re
import os

# if os.path.exists('qiushi.html'):
#     print('file already exist')
#     with open('qiushi.html', 'r') as f:
#         data = f.read()
# else:
#     r = requests.get('http://www.qiushibaike.com')
#     # print(r.content)
#     data = r.content.decode('utf-8')
#     with open('qiushi.html', 'w') as f:
#         f.write(data)

# soup = BeautifulSoup(data, 'html.parser')
# l = soup.find_all(attrs={'class': 'article block untagged mb15'})
# # tag = soup.a
# # print(tag.attrs)
# # print(tag.attrs)
# print(len(l))
# for i in l:
#     # print(i.find(attrs={'class': 'thumb'}))
#     if None != i.find(attrs={'class': 'thumb'}):
#         print('include image')
#     else:
#         print(i.find(attrs={'class': 'content'}).text.strip())
#     # pass


class crawler:
    def __init__(self):
        self.enable = True
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        self._page_now = 0
        self.story_list = []

    def load_page(self):
        if len(self.story_list) < 3:
            code = self.get_page_code(self._page_now + 1)
            if code != False:
                self.analysis_code(code)
                self._page_now += 1
            # print(self.story_list[0])

    def get_page_code(self, page_index=1):
        url = 'http://www.qiushibaike.com/hot/page/%d/' % page_index
        r = requests.get(url, headers=self.headers)
        if r.status_code != 200:
            print('Network Error')
            return False
        return r.content.decode('utf-8')

    def analysis_code(self, code='Not Data'):
        # code = self.get_page_code(page_index)
        soup = BeautifulSoup(code, 'html.parser')
        # print('analysis')
        temp_list = soup.find_all(
            attrs={'class': 'article block untagged mb15'})
        for story in temp_list:
            if None == story.find(attrs={'class': 'thumb'}):
                self.story_list.append(
                    story.find(attrs={'class': 'content'}).text.strip())

    def get_story(self):
        input_data = input()
        # print(input_data)
        if input_data == 'Q' or input_data == 'q':
            self.enable = False
            return
        self.load_page()
        # print('print story')
        if len(self.story_list) > 0:
            print(self.story_list[0])

    def start(self):
        print('正在读取，按回车键查看，Q键退出')
        self.load_page()
        while self.enable:
            self.get_story()
            del self.story_list[0]

if __name__ == '__main__':
    cra = crawler()
    cra.start()

# cra = crawler()
# cra.start()
