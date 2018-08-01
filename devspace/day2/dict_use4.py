#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng <shiwanyin199@gmail.com>

'''
字典的循环
'''

info = {
    'name1': 'lifangcheng',
    'name2': 'reckful',
    'name3': 'lfc'
}

print(info)

for i in info:
    print(i, info[i])

for k, v in info.items():
    print(k, v)
    # print(type(k))
    # print(type(v))
