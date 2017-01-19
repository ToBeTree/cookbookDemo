# import gevent
# import time
# import random
# start = time.time()
# tic = lambda: 'now 1.1f seconds' % (time.time() - start)


# def task(pid, name):
#     gevent.sleep(random.randint(0, 2) * 0.001)
#     print('task %d is Done' % pid)


# def syncchronous():
#     for i in range(1, 10):
#         task(i, i)


# def asyncchronous():
#     threads = [gevent.spawn(task, i, i) for i in range(1, 10)]
#     gevent.joinall(threads)
# # # print(tic)
# # print('sync')
# # syncchronous()
# # # print(tic)
# # print('async')
# # asyncchronous()

# import gevent
# from gevent.pool import Pool
# from gevent.lock import BoundedSemaphore
# import time
# sem = BoundedSemaphore(2)


# def worker1(n):
#     sem.acquire()
#     gevent.sleep(2)
#     if sem.counter <= 1:
#         print('no sigal, wait amount')
#         gevent.sleep(1)
#         sem.release()
#     # sem.release()


# def worker2(n):
#     gevent.sleep(2)
#     # a = sem.counter
#     # print(sem.counter)
#     # with sem:
#     #     print('%d ok' % n)
#     sem.acquire()
#     print('are you ok')
# tic = lambda: time.time()
# start = time.time()
# # print(start)
# pool = Pool(2)
# pool.map(worker1, range(0, 2))
# print(tic() - start)
# start = tic()
# pool.map(worker2, range(2, 4))
# # print(gevent.sleep(2))
# print(tic() - start)

from gevent.local import local

stash = local()
stash.y = 2

# from gevent.pywsgi
def f1():
    stash.x = 1
print(stash.y)
print(stash.x)
