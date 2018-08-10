#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng <shiwanyin199@gmail.com>

list1 = [1, 3, 2, 6, 7, 3, 4]
list2 = [9, 4, 5, 7, 3, 6, 1]

list1 = set(list1)
list2 = set(list2)

print(list1, list2)

print(list1 & list2)  # 并集
print(list1 | list2)  # 交集
print(list1 - list2)  # 差集(项在 list1中,但不在 list2中)
print(list1 ^ lists2)  # 对称差集(项在 list1 或 list2中, 但不会同时出现在二者中)
