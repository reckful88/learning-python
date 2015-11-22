#-*- coding: utf-8 -*-

'''
用函数和列表解析求和 乘积
'''

num1 = 0
num2 =1

for x in range(1,1001):
    num1 = num1 + x
    num2 = num2 * x
print num1,num2


#sum([x for x in range(1,1001)])     列表解析的方式求和，用sum这个内置函数。
