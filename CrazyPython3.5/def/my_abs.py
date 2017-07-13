#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
求绝对值函数，新增抛出异常功能
if not isintance(x, (int, float)) 这句话代表如果 x 不是 int 或者 float 则抛出异常信息
'''


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(10))
print(my_abs(-20))
print(my_abs('A'))
