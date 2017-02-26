from bs4 import BeautifulSoup
import requests
import re


class jiandan:
    def __init(self):
        pass
        # re.compile

    def get_response(self, url=''):
        url = 'http://jandan.net/ooxx/page-2357'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Host': 'jandan.net'
        }
        return requests.get(url, headers=headers).content

    def parse_html(slef, response):
        soup = BeautifulSoup(response, 'html.parser')
        # imgs = soup.find_all('li', id=re.compile('comment-[0-9]*'))
        imgs = soup.find_all('div', attrs={'class': 'text'})
        # 直接通过标签对象调用，会直接找到第一个符合条件的标签
        a = soup.ol
        print(a)
        print(len(imgs))
        for img in imgs:
            img_url = img.find('a').get('href')
            print(img_url)

if __name__ == '__main__':
    jd = jiandan()
    jd.parse_html(jd.get_response())
