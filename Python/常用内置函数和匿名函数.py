#!/usr/env python
# -*- coding:utf8 -*-
__author__ = '李国征'
__email__ = "745292907@qq.com"
########################################################################################################
# 版本: python 3.6
# 编辑日期: 2019/02/25
# 功能: 常用内置函数和匿名函数
# 依赖包: python
# 运行方法: python 常用内置函数和匿名函数.py
########################################################################################################


# zip
# ----- start -----
# zip相当于衣服的拉链，将一个list和另外list甚至多个list进行相扣
# a = [1, 2, 3]
# b = ["a", "b", "c"]
# print(zip(a, b))  # 即 生成器 可以通过dir查看是否包含__iter__方法
# cc = zip(a, b)
# for i in cc:
#     print(i)
# -----  end  -----


# filter
# ----- start -----
# 可以理解为查询搜索
# 方法 filter(func,list) func:必须为函数，list:列表（或容器类）
# 查找所在的字符串
# filter_a = [1, 2, 'hello', "", " ", 'woooooo']
# cc = filter(lambda x: str(x).strip() if type(x) == str else None, filter_a)
# for i in cc:
#     print(i)
# -----  end  -----


# sorted
# ----- start -----
# 排序，优点：排序速度快 比自己写的强很多基于c和系统，缺点：相对来说比较占内存，它会将结果写入一个新列表中。如果处理大数据时慎用
#
# sorted_a = [1, 5, 2, 9, -1, 30, -30]
# print(sorted(sorted_a))
# sorted_a.sort()
# print(sorted_a)
# -----  end  -----


# map
# ----- start -----
# cc_map = map(lambda x: x+x, [i for i in range(20)])
# print(cc_map)
# for i in cc_map:
#     print(i)
# -----  end  -----

# max
# ----- start -----
max(10, 20)
# key 值为函数
# -----  end  -----


# min
# ----- start -----
min(10, 20)
# key 值为函数
# -----  end  -----


# lamdba 匿名函数
# ----- start -----
cc_map = map(lambda x: x+x, [i for i in range(20)])
print(cc_map)
for i in cc_map:
    print(i)
# -----  end  -----




