import requests
import re
from bs4 import BeautifulSoup
from lxml import html
# from html.parser import HTMLParser
# this module is solve InsecureRequestWarning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class crawler():
    def __init__(self):
                # self.host = 'https://www.zhihu.com'
        self.cookies = {'d_c0': '"AJACQd-u6gqPTjLVHnl-SOY6xBAgrm_zuAk=|1480328007"',
                        '_zap': '79ef8fea-9c4a-4482-a878-47db266d2ca4',
                        'q_c1': 'a6de68fca7384301a06898f219e7e4d7|1483434661000|1480328006000',
                        '_xsrf': '46572bcb45716b6acbdb7b04d3dea747',
                        'aliyungf_tc': 'AQAAAL9LKhZwkAAA4y1uJFjvsiB6l1Yo',
                        'l_n_c': '1',
                        'l_cap_id': '"NmI0NjBhOWEzMmM5NDBiZjhkMmUxYjY4NmJjNWEzMGQ=|1484548662|d962a227b911ae017e62ba310424ff212f9a14af"',
                        'cap_id': '"YzA1ZTdjZWI1NjlkNDY4OGE5ZjFjMDhkMjc3YjkwZWU=|1484548662|498a769644d776800711f754669a77e21689baff"',
                        'r_cap_id': '"MDJjMWMxNmQyYThlNGQyOWJhYjM5M2M5NTZhOTQwNzk=|1484548663|deb7a4b64e64ad73b93817332af64f3d0387ec39"',
                        'login': '"ZjkwOGNlYzBiM2Y1NGM5MDg1NTI0Njc0NDNjNmY1MGU=|1484548695|3934a9f4a3a9b475b17a814b7b1d2d2e721ea2cf"',
                        '__utma': '51854390.1812732108.1484548241.1484548241.1484548241.1',
                        '__utmb': '51854390.0.10.1484548241',
                        '__utmc': '51854390',
                        '__utmz': '51854390.1484548241.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/tobetree/collections',
                        '__utmv': '51854390.100-1|2=registration_date=20150803=1^3=entry_date=20150803=1',
                        'z_c0': 'Mi4wQUJCTV9vX2VmQWdBa0FKQjM2N3FDaGNBQUFCaEFsVk5WX2VqV0FCOUkxd21SdVJEVkVXU1hmRFY5bTZ6VVFVemV3|1484549220|38d793ff4a376c4cd95a2a629647042d0e176a4c'
                        }
        self.headers = {}
        self.headers[
            'Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        self.headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        self.headers['Host'] = 'www.zhihu.com'
        self.headers['Referer'] = 'www.zhihu.com'

    def send_requests(self, url):
        try:
            r = requests.get(url, cookies=self.cookies,
                             headers=self.headers, verify=False)
        except:
            print('error')
            return False
        if r.status_code == 200:
            print('success')
            # t = html.html_parser(r.text)
            tree = html.fromstring(r.text)
            print(tree.xpath("//h2[@class='ContentItem-title']//a[@class='UserLink-link']/@href"))
            # print(tree.xpath("//span[@class='location item']/@title"))
            # print(r.text)
            # html_parser = HTMLParser.HTMLParser()
            # txt = HTMLParser.unescape(r.content)
            # self.analysis_profile(r.text)
            return True

    def analysis_profile(self, data):

        soup = BeautifulSoup(data, 'html.parser')
        name_list = soup.find_all(attrs={'class': 'ContentItem-title'})
        # name_list = soup.select('.UserLink-link')
        print(len(name_list))
        for name in name_list:
            print(name.find('a')['href'])

if __name__ == '__main__':
    c = crawler()
    c.send_requests('https://www.zhihu.com/people/gaoming623/following')
