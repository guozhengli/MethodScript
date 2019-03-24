#!/usr/env python
# -*- coding:utf8 -*-
__author__ = '李国征'
__email__ = "745292907@qq.com"
########################################################################################################
# 版本: python 3.6
# 编辑日期: 2019/02/25
# 功能: 使用docx
# 依赖包: python
# 运行方法: python docx处理.py
########################################################################################################

from docx import Document

base_list = ["个人信息", "专业技能", "项目经验", "教育背景", "求职意向", "个人评价"]

# son_list = ["姓名", "性别", "年龄", "学历", "籍贯", "邮箱", "联系电话", "现居地址",]

split_list = ["个人信息"]  # 需要拆分列表

dct = {}

document = Document(u'/tmp/tt/111.docx')


l = [paragraph.text for paragraph in document.paragraphs];


def Subcontracting(list_str):
    # 根据base list 关键词进行分包处理
    tmp_index = []
    for prh in list_str:
        if prh in base_list:
            # tmp_index.append(base_list.index(prh.strip()))
            tmp_index.append(list_str.index(prh))
    sorted(tmp_index)
    # print(len(tmp_index))
    # print(list_str[tmp_index[0]:tmp_index[1]])
    # print(list_str[tmp_index[1]:tmp_index[2]])
    # print(list_str[tmp_index[2]:tmp_index[3]])
    # print(list_str[tmp_index[3]:tmp_index[4]])
    # print(list_str[tmp_index[4]:tmp_index[5]])
    # print(list_str[tmp_index[5]:])
    # print(tmp_index)
    for i in tmp_index:
        if int(tmp_index.index(i)+1) == len(tmp_index):
            print(list_str[i:])
        else:
            # print(i, tmp_index[int(tmp_index.index(i)+1)])
            subs = tmp_index[int(tmp_index.index(i)+1)]
            print(list_str[i:subs])


def test1(hang):
    aa = hang.split("\t")
    tmp_dict = {}
    return filter(lambda x: tmp_dict.update({x.split("：")[0]: x.split("：")[1]}) if "：" in x else None, aa)



Subcontracting(l)


