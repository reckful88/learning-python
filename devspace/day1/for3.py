#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng

'''
循环套循环
'''

for i in range(10):
    print('-----------', i)
    for j in range(10):
        print(j)
        if j > 5:
            break