#!/usr/env python
# -*- coding:utf8 -*-
__author__ = '李国征'
__email__ = "745292907@qq.com"
########################################################################################################
# 版本: python 3.6
# 编辑日期: 2019/02/25
# 功能: 生成器yield使用的使用
# 依赖包: python
# 运行方法: python 生成器.py
########################################################################################################

# 生成器简易使用
# ----- start -----
"""
个人理解：
    for 循环只循环可迭代的
    for 循环时先判断的是否含有yield的 如果不是直接报错
    yield 相当于return 的功能，只不过 return是直接返回了 而yield 返回了但是再次使用还会在原yield点继续执行
    send()功能
        首次调用必须是next的 
        最后一次必须不能是send
        send("内容") 可以send进去内容 内容位置就是在上一次yield的位置开始
"""


# def func():
#     print(1111)
#     yield 1
#     print(2222)
#     yield
#
# ret = func()
# ret.__next__()  # 11111 1
# ret.__next__()  # 2222 2
# ret.__next__()  # 报错 StopIteration

# send的简易使用
# def func():
#     print(1111)
#     ret = yield 1
#     print(ret,'aaaaa')
#     print(2222)
#     yield
#
# ret = func()
# ret.__next__()
# ret.send("我应该在1后面")
# -----  end  -----


# 移动求平均值
# 利用 装饰器和 生成器实现移动平均值
# ----- start -----

# def init(f):    # 这步起的作用是减少用户不友好的多次输入next，而且后期大量使用时直接调用即可
#     def inter():
#         fu = f()
#         fu.__next__()
#         return fu
#     return inter
#
#
# @init
# def func():
#     sum = 0
#     count = 0
#     arg = 0
#     while True:
#         num = yield arg # 将每一次的send 值赋值给上一次yield结束的位置，即num= send(数据)
#         sum += num
#         count += 1
#         arg = sum/count
#
#
# a = func()
# cc = a.send(10)
# ss = a.send(30)
# print(ss)

# -----  end  -----






