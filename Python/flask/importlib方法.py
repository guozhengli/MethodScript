#!/usr/env python
# -*- coding:utf8 -*-
__author__ = '李国征'
__email__ = "745292907@qq.com"
########################################################################################################
# 版本: python 3.6
# 编辑日期: 2019/04/03
# 功能: 根据django源码引申出的一个使用方法，就是django setting中的中间件调用方法 是使用这种方式
#       midd = [
#           "myobject.MyClass",
#       ]
# 依赖包: python
# 运行方法: python decorator.py
########################################################################################################


# importlib 方法实现
# ----- start -----





# -----  end  -----

# 仿threading.local 方法实现
# ----- start -----
# 写一个多线程 给每个多线程分配内存空间，解除锁相关概念什么的 其实就是 写一个object 引入__setitem__方法来实现 dict方法




# -----  end  -----
