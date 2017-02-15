import requests


headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI MAX Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.5.908 Mobile Safari/537.36'
res = requests.get('http://m.uatplus.com', headers=headers)
if res.status_code == 200:
    cookies = res.cookies.get_dict()
    print('status_code %s' % res.status_code)
    print(cookies)
    headers['Referer'] = 'http://m.uatplus.com/'
    headers['Host'] = 'm.uatplus.com'
    r = requests.get(
        'http://m.uatplus.com/index/getHotCircleTemplet', headers=headers, cookies=cookies)
    print(r.content.decode('utf-8'))
