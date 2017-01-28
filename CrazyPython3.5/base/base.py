#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 输出 print

'''
输出 print
'''
print('hello, world')

'''
print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出：
'''

print('the quick brown fox', 'jump over', 'the lazy dog')

'''
print()会依次打印每个字符串，遇到逗号“,”会输出一个空格，因此，输出的字符串是这
样拼起来的：
'''

print ('the quick brown fox,', 'jump over', 'the lazy dog')

'''
print 也可以打印整数或计算结果
'''

print (300)
print (300 + 200)
print ('300 + 200 =',  300 + 200)

# 输入 input

'''
name = input()
print ('hello,', name)
'''

# name = input('please enter your name:')
# print ('your name is:', name)

'''
练习：
请利用print()输出1024 * 768 = xxx
'''

print ('1024 * 768 =', 1024 * 768)

# 数据类型

'''
整数：1, 100, -8080, 0
浮点数：1.23, 3.14, -9.01
字符串：用单引号或者双引号引起来的的任意文本
'''

print ('I\'m \"OK\"!')
print ('I\'m learning\npython.')
print ('\\\n\\\\')

'''
布尔值：True False
'''

print (True)
print (False)
print (3 > 2)
print (3 > 5)

'''
布尔值可以用 and 、or 、not 运算

 `and`运算是与运算，只有所有都为`True`，`and`运算结果才是`True`：
`or`运算是或运算，只要其中有一个为`True`，`or`运算结果就是`True`：
`not`运算是非运算，它是一个单目运算符，把`True`变成`False`，`False`变成`True`：
'''

print (True and True)
print (True and False)
print (False and False)
print (5 > 3 and 3 > 1)
print (True or True)
print (True or False)
print (False or False)
print (5 > 3 or 1 > 3)
print (not True)
print (not False)
print (not 1 > 2)

'''
空值：None    None不能理解为0， 0 是有意义的，而None就是一个特殊的空值
'''

# 变量、格式化

'''
变量名必须是大小写英文、数字和`_`的组合，且不能用数字开头

同一个变量可以反复赋值，而且可以是不同类型的变量
'''
a_test = 'ABC'
b_test = a_test
a_test = 'XYZ'
print (b_test)

'''
格式化
'''
