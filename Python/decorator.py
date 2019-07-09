#!/usr/env python
# -*- coding:utf8 -*-
__author__ = '李国征'
__email__ = "745292907@qq.com"

########################################################################################################
# 版本: python 3.6
# 编辑日期: 2019/02/25
# 功能: 装饰器的使用
# 依赖包: python
# 运行方法: python decorator.py
########################################################################################################

# 简易装饰器
# ----- start -----
# 语法糖 @
"""
步骤说明：
    1、@witer ==> func = witer(func)
    2、装饰器 函数 套函数 里面函数要return 
"""
import time
#
#
# def witer(f):
# #     def inter():
# #         start = time.time()
# #         f()
# #         end = time.time()
# #         print(end - start)
# #     return inter
#
#
# @witer
# def func():
#     print("我就是一个简易的被装饰器函数")
#
#
# func()  # inter

# -----  end  -----


# 被装饰器函数 带参数
# ----- start -----
# import time
#
#
# def witer(f):
#
#     def inter(*args, **kwargs):
#         start = time.time()
#         ret = f(*args, **kwargs)
#         end = time.time()
#         print(end - start)
#         return ret
#
#     return inter
#
# @witer
# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     print("我就是带了个参数的被装饰器函数")
#
# func("aa")

# -----  end  -----


# 装饰器带参数
# ----- start -----
"""
说明：
    装饰器带参数的话 可以这么理解就行了
    同上一个带参数的装饰器。而这个装饰器就是在那个装饰器上边套了一个普通函数。可以将语法糖分解这么看
    @witer_out ==> witer_out = witer(f)
    理解就是将一个最外面函数里面套了一个装饰器
    分解为 @ witer_out  先执行witer_out 然后在语法糖@ 
"""


# def witer_out(*args, **kwargs):
#     print(args)
#
#     def witer(f):
#         def inter(*args, **kwargs):
#             start = time.time()
#             ret = f(*args, **kwargs)
#             end = time.time()
#             print(end - start)
#             return ret
#         return inter
#     return witer
#
#
# @witer_out("bb")
# def func(*args, **kwargs):
#     print("我就是带了个参数的被装饰器函数")

# func("aa")
# -----  end  -----

# 多装饰器
# ----- start -----

def zsj1(f): # func

    def inter1():
        print('装饰器1 start')
        f()
        print('装饰器1 end')
    return inter1


def zsj2(f): # f == inter1
    def inter():
        print('装饰器2 start')
        f()  # inter1
        print('装饰器2 end')

    return inter


@zsj2 # 在把inter1 传入这个里面执行
@zsj1   # == zsj1 = zsj1(func) == inter1
def func():
    print("i am func hohah")


func()

# -----  end  -----

