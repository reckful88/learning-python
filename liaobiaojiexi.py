# -*- coding: utf-8 -*-

'''
计算出1x1 2x2 3x3 ... 10x10
先用for循环的方法，记得append
'''

L = []

for x in range(1,11):
    L.append(x * x)

print L
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''
用列表解析的方法就简单了，
[x * x for x in range(1,11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
