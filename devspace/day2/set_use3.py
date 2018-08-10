#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng <shiwanyin199@gmail.com>

list1 = [1, 3, 2]
list2 = [9, 2, 5]

list1 = set(list1)
list2 = set(list2)

print(list1, list2)

list1.add(999)  # 添加一项
print(list1)

list2.update([11, 22, 33, 'haha', 'hehe'])  # 添加多项
print(list2)

print(len(list2))  # 计算 set 的长度

print(list1 in list2)  # 判断 list1 是否是 list2 的成员
print(list1 not in list2)  # 判断 list1 是否不是 list2 的成员

print(list2.pop())  # 随机删除一个集合中的元素并返回
print(list2.remove('hehe'))  # 删除一个集合中的指定元素
print(list2)

'''
删除一个集合中的指定元素, 
和 remove 的区别是: 如果要删除的那个元素不在集合中, remove 会报错, discard 不会
'''
print(list2.discard('haha'))
print(list2)
print(list2.discard('haha'))
