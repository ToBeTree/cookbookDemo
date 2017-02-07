import os
from bs4 import BeautifulSoup
import requests

class crawler:
	def __init__(self):
		self.cookies={
		'userFromPsNeedShowTab':'1',
		'BAIDUID':'17A7EFE7B3FF17A070C9EBD6EFD7573C:FG=1',
		'TIEBA_USERTYPE':'a909e9f70ca68f6378fc4dcf',
		'bdshare_firstime':'1480384961354',
		'PSTM':'1480471112',
		'BIDUPSID':'50035E39137029DAD844FC3AE7EEC4DE',
		'TIEBAUID':'9be462d303c9680779eceffd',
		'MCITY':'-131%3A',
		'pgv_pvi':'2572294144',
		'wise_device':'0'
		}
		self.headers={}
		# self.headers['Host']='tieba.baidu.com'
		self.headers['User-Agent']='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

	def send_requests(self,url):
		r = requests.get(url,headers=self.headers,cookies=self.cookies)
		soup = BeautifulSoup(r.content,'html.parser')
		imgs = soup.find_all(attrs={'class':'BDE_Image'})
		# imgs = soup.find_all('img',class_='DBE_Image')
		for img in imgs:
			# print(img.get('src'))
			print('-'*40)
			print('开始下载',img.get('src').split('/')[-1])
			self.download_image(img.get('src'))
			# print('下载完成')
	def download_image(self, url):
		if os.path.exists('img/'+url.split('/')[-1]):
			print('此文件已存在路径中！')
			print('下载完成')
		else:
			r = requests.get(url,cookies=self.cookies,headers=self.headers)
			if r.status_code == 200:
				with open('img/'+url.split('/')[-1],'wb') as f:
					f.write(r.content)
				print('下载完成')
			else :
				print('请求失败!')
if __name__ == '__main__':
	c = crawler()
	c.send_requests('http://tieba.baidu.com/p/4023230951')

