#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng <shiwanyin199@gmail.com>

'''
集合是一个无序的, 不重复的数据组合, 它的主要作用如下:

1. 去重, 把一个列表变成集合, 就自动去重了
2. 关系测试, 测试两组数据之间的交集, 差集, 并集等关系
'''

# 去重

name = ['lfc', 'lfc', 'reckful', 'haha', 'lfc']
print(name)
set_name = set(name)
print(set_name, type(set_name))

# 取交集(合并起来找到重复的)

list1 = [1, 3, 2, 6, 7, 3, 4]
list2 = [9, 4, 5, 7, 3, 6, 1]
print(list1, list2)
print(set(list1).intersection(set(list2)))

# 并集(合并起来去掉重复的)

list1 = [1, 3, 2, 6, 7, 3, 4]
list2 = [9, 4, 5, 7, 3, 6, 1]
print(set(list1).union(set(list2)))

# 差集(我有你没有,或者你有我没有的元素,找出不同)

list1 = [1, 3, 2, 6, 7, 3, 4]
list2 = [9, 4, 5, 7, 3, 6, 1]
print(set(list1).difference(set(list2)))
print(set(list2).difference(set(list1)))

# 子集(是否包含一个集合)

list1 = [1, 3, 2, 6, 7, 3, 4]
list2 = [9, 4, 5, 7, 3, 6, 1]
print(set(list1).issubset(set(list2)))  # 判断 list2 是不是 list1 的子集

# 父集

list1 = [1, 3, 2, 6, 7, 3, 4]
list2 = [9, 4, 5, 7, 3, 6, 1]
print(set(list1).issuperset(set(list2)))  # 判断 list2 是不是 list1 的父集

# 对称差集
print(set(lit1).symmetric_difference(set(list2)))  # 取出这两个集合内都互相没有的元素
