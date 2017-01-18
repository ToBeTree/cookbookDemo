# import gevent
# from gevent.event import Event

# evt = Event()


# def setter():
#     print('wait for me')
#     gevent.sleep(3)
#     print('i am ok')
#     evt.set()


# def waiter():
#     print('i wait for you ')
#     evt.wait()
#     print('it is about time')


# def main():
#     gevent.joinall([
#         gevent.spawn(waiter),
#         gevent.spawn(setter),
#         gevent.spawn(waiter),
#         gevent.spawn(waiter),
#         gevent.spawn(waiter)
#     ])

# # from gevent import Timeout

# # seconds = 2

# # timeout = Timeout(seconds)
# # timeout.start()


# # def wait():
# #     gevent.sleep(1)

# # try:
# #     gevent.spawn(wait).join()
# # except Timeout:
# #     print('Could not complete')
# if __name__ == '__main__':
#     main()

# import gevent
# from gevent.event import AsyncResult
# a = AsyncResult()


# def setter():
#     """
#     After 3 seconds set the result of a.
#     """
#     gevent.sleep(3)
#     a.set('Hello!')


# def waiter():
#     """
#     After 3 seconds the get call will unblock after the setter
#     puts a value into the AsyncResult.
#     """
#     print(a.get())

# gevent.joinall([
#     gevent.spawn(setter),
#     gevent.spawn(waiter),
# ])

import gevent
from gevent.pool import Pool
pool = Pool(2)


def hello_from(n):
    # print(n)
    print('size of %s' % len(pool))
pool.map(hello_from, range(0, 3))
