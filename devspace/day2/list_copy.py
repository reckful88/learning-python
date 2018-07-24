#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng <shiwanyin199@gmail.com>

'''
浅 copy 的三种方式
'''

import copy

person = ['name', ['a', 100]]

p1 = copy.copy(person)
p2 = person[:]
p3 = list(person)

print(p1, p2, p3)