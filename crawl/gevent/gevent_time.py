import time


def echo(i):
    time.sleep(0.001)
    return i
# from multiprocessing.pool import Pool
# p = Pool(4)
# run1 = [a for a in p.imap_unordered(echo, range(1, 10))]
# run2 = [a for a in p.imap_unordered(echo, range(1, 10))]
# run3 = [a for a in p.imap_unordered(echo, range(1, 10))]
# run4 = [a for a in p.imap_unordered(echo, range(1, 10))]

# print(run1 == run2 == run3 == run4)


from gevent.pool import Pool

p = Pool(4)
run1 = [a for a in p.imap_unordered(echo, range(1, 10))]
run2 = [a for a in p.imap_unordered(echo, range(1, 10))]
run3 = [a for a in p.imap_unordered(echo, range(1, 10))]
run4 = [a for a in p.imap_unordered(echo, range(1, 10))]

# print(run1 == run2 == run3 == run4)
import gevent
from gevent import Greenlet


def foo(message, n):
    gevent.sleep(n)
    print(message)

t1 = Greenlet.spawn(foo, 'hello', 1)
t2 = gevent.spawn(foo, 'world', 2)
t3 = gevent.spawn(lambda x: x + 1, 2)
threads = [t1, t2, t3]
# gevent.joinall(threads)

from gevent import Timeout


def wait():
    gevent.sleep(2)
timer = Timeout(1).start()
thread1 = gevent.spawn(wait)
try:
    thread1.join(timeout=timer)
except Timeout:
    print('Thread1 timeout')

try:
    gevent.with_timeout(1, wait)
except:
    print('Thread3 timeout')
