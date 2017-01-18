import gevent
import time
import random
start = time.time()
tic = lambda: 'now 1.1f seconds' % (time.time() - start)


def task(pid, name):
    gevent.sleep(random.randint(0, 2) * 0.001)
    print('task %d is Done' % pid)


def syncchronous():
    for i in range(1, 10):
        task(i, i)


def asyncchronous():
    threads = [gevent.spawn(task, i, i) for i in range(1, 10)]
    gevent.joinall(threads)
# # print(tic)
# print('sync')
# syncchronous()
# # print(tic)
# print('async')
# asyncchronous()
