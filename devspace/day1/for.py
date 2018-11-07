#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng

# contine

'''
contine 和 break 的区别：

contine： 结束当前循环，进入下一次循环
break：跳出当前循环
'''

for i in range(0, 10):
    if i < 5:
        print("loop", i)
    else:
        continue
    print("lalala...")
