#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng <shiwanyin199@gmail.com>


'''
copy 的用法 (浅copy)
'''

names = ['lfc', 'lifangcheng', 'reckful', 'jack', 'tom', 'bob']

names2 = names.copy()
print(names)
print(names2)

names[3] = 'Jack'
print(names)
print(names2)


'''
列表中套列表
'''

names = ['lfc', 'lifangcheng', 'reckful', ['jack', 'tom'], 'bob']
print(names)
names[3][0] = 'Jack'
print(names)
names.insert(1, ['aaa','bb','cc'])
print(names)

'''
深 copy, 完整 copy
'''

import copy

names2 = copy.deepcopy(names)
print(names)
print(names2)


'''
循环列表
'''

for i in names:
    print(i)