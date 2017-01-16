# import multiprocessing
import requests
import os
import time
from multiprocessing import Pool

urls = []


def get_source(url):
    # print('start request')
    html = requests.get(url)
    print(html.url)
    print(os.getpid())

# time1 = time.time()


# time2 = time.time()
# print('it take: %s' % (time2 - time1))

if __name__ == '__main__':
    # print(os.getpid())
    # requests.get('http://tieba.baidu.com/p/3522395718?pn=1')
    for i in range(1, 10):
        new_page = 'http://tieba.baidu.com/p/3522395718?pn=%s' % str(i)
        urls.append(new_page)

    pool = Pool(4)
    time1 = time.time()
    for url in urls:
        get_source(url)
        # pool.apply_async(get_source, args=(url,))
    time2 = time.time()
    print('11it take: %s' % (time2 - time1))
    time1 = time.time()
    pool.map(get_source, urls)
    pool.close()
    pool.join()
    time2 = time.time()
    print('it take: %s' % (time2 - time1))
    print('Done')
