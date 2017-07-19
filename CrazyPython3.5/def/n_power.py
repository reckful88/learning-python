# -*- coding: utf-8 -*-

'''
计算任意一个数的n次方
2，3  就是2的3次方
'''


def power(x, y):
    return x ** y


print (power(2, 3))


'''
方法二：
def power(x, y):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
'''
