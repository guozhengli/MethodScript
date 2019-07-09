#!/usr/env python
# -*- coding:utf8 -*-
__author__ = '李国征'
__email__ = "745292907@qq.com"

########################################################################################################
# 版本: python 3.6
# 编辑日期: 2019/02/25
# 功能: 命名空间的定义与说明
# 依赖包: python
# 运行方法: python 线程.py
########################################################################################################


"""
进程：
    进程 资源调度，开辟空间等资源
    守护进程：主进程代码执行完毕后 守护线程随即完成，不管开启守护进程的代码执行完没有 即 主进程执行完毕后 守护进程随即完成 退出
线程
    线程 调度， 每一个进程会开起一个主线程，代码执行是主线程执行的。
    守护线程：主线程执行代码完毕后 等待其他非守护线程的线程完毕后 退出 如果此时其他线程没有完成时 守护线程代码能够执行完毕时，继续执行。
    如果其他线程完成时 守护线程没有完成时，即退出
"""


# from threading import Thread, currentThread

# 开启20 个线程 打印线程名
# def func():
#     print(currentThread().getName())
#
# for i in range(20):
#     t = Thread(target=func)
#     t.start()

# 线程锁
# from threading import Thread, Lock, currentThread
# lock = Lock()
# import time
# import random
#
# def func():
#     lock.acquire()
#     time.sleep(random.randint(1,3))
#     print(currentThread().getName())
#     lock.release()
#
# for i in range(10):
#     t = Thread(target=func)
#     t.start()


# 死锁
# from threading import Thread, Lock, currentThread
# lockA = Lock()
# lockB = Lock()
# import time


# 这种效果 就是 死锁 因为f1 Thread-1 拿了一个钥匙，又拿了第二个钥匙 然后释放后 f2 又拿了第二个钥匙后停了1秒 此时f1 Thread-2拿到第一把钥匙
# f2 停了1秒后 想拿第一把钥匙 此时Thread-2 拿着第一把钥匙等待拿第二吧钥匙 即死锁了
# print info
# 我是A Thread-1
# 我是B Thread-1
# 我是B Thread-1
# 我是A Thread-2

# class MyThread(Thread):
#     def run(self):
#         self.f1()
#         self.f2()
#
#
#     def f1(self):
#         lockA.acquire()
#         print('我是A %s' %currentThread().getName())
#         lockB.acquire()
#         print('我是B %s' % currentThread().getName())
#         lockB.release()
#         lockA.release()
#
#
#     def f2(self):
#         lockB.acquire()
#         print('我是B %s' %currentThread().getName())
#         time.sleep(1)
#         lockA.acquire()
#         print('我是A %s' % currentThread().getName())
#         lockA.release()
#         lockB.release()


# for i in range(10):
#     t = MyThread()
#     t.start()

# 递归锁(互斥锁) 解决死锁问题 设置一个内部计数器来计数锁数量，如果不为0时 则其他线程获取不到 直到为0时 其他线程才可进行
# from threading import Thread, RLock, currentThread
# lock = RLock()
# import time
# class MyThread(Thread):
#     def run(self):
#         self.f1()
#         self.f2()
#
#
#     def f1(self):
#         lock.acquire()
#         print('我是A %s' %currentThread().getName())
#         lock.acquire()
#         print('我是B %s' % currentThread().getName())
#         lock.release()
#         lock.release()
#
#
#     def f2(self):
#         lock.acquire()
#         print('我是B %s' %currentThread().getName())
#         time.sleep(1)
#         lock.acquire()
#         print('我是A %s' % currentThread().getName())
#         lock.release()
#         lock.release()
#
# for i in range(10):
#     t = MyThread()
#     t.start()

# 线程池和信号量的区别？
# 信号量 是开启一批线程后 给了几把锁(这个锁的数量是你设定信号量里面的那个数值决定)
# 线程池 设定几个线程就只开启这几个线程。

# 信号量
# from threading import Thread, Semaphore, currentThread
# import time
#
#
# def func():
#     with sm:
#         print('我是: %s' % currentThread().getName())
#         time.sleep(5)
#
#
# sm = Semaphore(5)   # 5个 5个的执行
# for i in range(10):
#     Thread(target=func).start()


# 线程池
from concurrent import futures

# futures.ThreadPoolExecutor 线程池
# futures.ProcessPoolExecutor 进程池

# def func(args):
#     print('aaaaa', args)
#
#
# ft = futures.ThreadPoolExecutor(5)
# for i in range(20):
#     t = ft.submit(func, i)
#     t.result()

# ft.map(func, range(10))    # 实现了 submit result 方法 但是不能获取 return 值

# 线程池 回调函数
# 起一个线程 将线程触发的函数object反馈给call函数
# from concurrent import futures
#
# def func(args):
#     return args+1
#
# def call(c):
#     print(c.result())
#
# ft = futures.ThreadPoolExecutor(5)
# for i in range(20):
#     ft.submit(func, i).add_done_callback(call)

# ######################练习#################################
# 打印 1 到 1000

# from threading import Thread, Semaphore
# import time
# import random
#
#
# def func(i):
#     s.acquire()
#     print(i)
#     time.sleep(random.randint(1, 3))
#     s.release()
#
#
# s = Semaphore(10)
# for i in range(1000):
#     t = Thread(target=func, args=(i,))
#     t.start()


