#!/usr/env python
# -*- coding:utf8 -*-
__author__ = '李国征'
__email__ = "745292907@qq.com"

import random
import time

# print(' 装饰器 '.center(100, '#'))


def func_call(f):
    def cc():
        start = time.time()
        f()
        end = time.time()
        t = end - start
        print(t)
    return cc


@func_call
def func():
    time.sleep(random.randint(1, 3))
    print('hello world')

# func()

# print(' 带参数的装饰器 '.center(100, '#'))


def func_args(*args, **kwargs):

    def func_call(f):
        # print(args)
        def cc():
            start = time.time()
            f()
            end = time.time()
            t = end - start
            print(t)
        return cc

    return func_call


@func_args("nihao")
def func():
    time.sleep(random.randint(1,2))
    print("hell world args..")

# func()


print(' 线程 '.center(100, '#'))

from threading import Thread
# 开启20个线程

def func(args):
    print(i)


# for i in range(20):
#     p1 = Thread(target=func, args=(i,))
#     p1.start()


# 带锁
from threading import Lock


def func():
    global n
    lock.acquire()
    temp = n
    time.sleep(random.randint(1,3))
    n = temp + 1
    print(n)
    lock.release()


p_lst = []
lock = Lock()
n = 0
# for i in range(10):
#     p1 = Thread(target=func)
#     p1.start()
#     p_lst.append(p1)
# #
# [i.join() for i in p_lst]
# print(n)

# 线程池
# from concurrent import futures
# p = futures.ThreadPoolExecutor(3)
#
# # for i in range(100):
# #     p1 = p.submit(func, i)
# #     p1.result()
#
# import time
# import random
# thread_tool = futures.ThreadPoolExecutor(10)
#
# f_lst = []
#
# def funcname(i):
#     print(i)
#     time.sleep(random.random())
#     return i*'*'
#
# def call(i):
#     print(i.result(),'ddddddd')
#
# for i in range(1000):
#     f = thread_tool.submit(funcname, i)
#     f_lst.append(f)
#     # f.result()
#
# [i.result() for i in f_lst]

# 生成器

# def funcb():
#     print(1111)
#     ret = yield
#     print(ret,'aaaaa')
#     print(2222)
#     yield
#
# a = funcb()
# a.__next__()
# a.send(1111)

# 装饰器
# def zsq(f):
#     def cc():
#         print('hahaha')
#         f()
#         print('heihei')
#     return cc
#
# @zsq
# def haha():
#     print('nihao')
#
# haha()

