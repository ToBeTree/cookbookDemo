import requests
import os
import time
from bs4 import BeautifulSoup

# https://book.douban.com/tag/
# https://book.douban.com
url = 'https://book.douban.com/tag/'
headers = {}
headers[
    'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')

tag_list = soup.find_all('a', attrs={'class': 'tag-title-wrapper'})
for tag in tag_list:
    # print(tag.get('name'))
    pass

cols = soup.find_all(attrs={'class': 'tagCol'})
for col in cols:
    c = col.find_all('td')
    print(len(c))
    for a in c:
        print(a.get_text() + ':' + a.find('a').get('href'))
