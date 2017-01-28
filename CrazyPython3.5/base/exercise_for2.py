# -*- coding: utf-8 -*-


"""
计算1~6的阶乘  1 x 2 x 3 x 4 x 5 x 6
"""

sum = 1
for x in range(1, 6):
    sum = sum * x
print(sum)


sum_a = str(sum)  # 转换成str
print (len(sum_a))  # 测出长度
sum_a_len = 0  # 新赋值

for i in sum_a:
    sum_a_len = sum_a_len + 1
print(sum_a_len)


"""
用for循环的方式，测出一个字符串的长度
"""
a = '123456789'  # 这是一个str
lens = 0
for x in a:
    lens = lens + 1
print(lens)
