import requests


class gome:
    def __init__(self):
        self.cookies = {
            'ssid': '677460592240.1480410924799',
            'Hm_lvt_4d914dda44888419a4588c6a4be8edcc': '1484623045',
            'mx_wap_gomeplusid': 'hasempdk0bdp96veinmr57e3e7',
            'isnew': '31599418440.1484809429187',
            'mx_wap_userId': '77f5lDT6uZzwVzSPAq%2BNYxXkDo%2BbwHRcd1zR%2Fr3o3jG5%2Fr0',
            'mx_wap_nickName': '9bb6iBUsiB96tS5D0LnETSZjI94t1q1Nu9O0q5Zm6S0Vqbpyh4mpvTsi',
            'plasttime': '1484809472'
        }
        self.headers = {}
        self.headers[
            'User-Agent'] = 'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
        self.headers['Content-Length'] = '7'
        self.headers['Host'] = 'm.gomeplus.com'
        self.headers['Content-Type'] = 'application/x-www-form-urlencoded'

    def send_request(self, url):
        payload = {'count': 2}
        r = requests.post(url, cookies=self.cookies,
                          headers=self.headers, data=payload)
        print(r.status_code)
        a = r.content.decode('utf-8')
        # print(a['msg'])
if __name__ == '__main__':
    g = gome()
    g.send_request('https://m.gomeplus.com/op/luckymoney/doDrawPrize')
