#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng <shiwanyin199@gmail.com>

'''
str 字符串的常用操作
'''

name = "my name is lifangcheng"

print(name.capitalize())  # 首字母大写
print(name.count('n'))  # 统计一个字符串内有多少个字母或者其他信息
print(name.center(50, '-'))  # 打印50个'-', 把变量 name 的信息放在横杠的中间
print(name.endswith('eng'))  # 判断一个字符串是不是以某些字符结尾
print(name.find('name'))  # 取出切片的值

'''
字符串格式化

name1 = 'my name is {name} and i am {year} old'
print(name.format(name='lifangcheng', year=26))
print(name.format_map( {'name':'alex', 'year':12})  # str.format_map 字典的方式 format
'''

print('abc123'.isalnum())  # 检查字符串内是否包括特殊字符, 如果不包括返回 True
print('abc123!#$%'.isalnum())
print(name.isdigit())   # 判断字符串内容是否是一个整数
print(name.isidentifier())  # 判断是不是一个合法的标识符(合法的变量名)
print(' '.isspace())    # 判断字符串内容是否是空格
print(''.join(['1', '2', '3', 'abc', 'bbc']))   # 把列表转成字符串
print('+'.join(['1', '2', '3', 'abc', 'bbc']))  # 每个字符串中间加一个区分的自定义符号
print(name.ljust(50, '*'))  # 字符串长度50,如果长度不够,在结尾用*号补齐, 长度和补齐的符号可以自定义
print(name.rjust(50, '-'))  # 与 ljust 相反,这个补齐在开头, 长度和补齐的符号可以自定义
print('Reckful'.lower())    # 字符串里的所有字母变小写
print('Reckful'.upper())    # 字符串里的所有字母变大写
print('\nReckful'.lstrip()) # 去掉最左边的空格或者回车
print('\nReckful'.rstrip()) # 去掉最右边的空格或者回车
print('\nReckful\n'.strip())    # 去掉两边的空格或者回车
print('Reckful'.replace('f', 'F', 1)) # 把字符串内的字符替换成指定字符, 如果只想替换一个, 后面写上具体数字
print('my name is lfc'.split(' '))    # 把字符串按照指定字符分割成一个列表,可以用空格为分隔符
print('1+2+3+4+5'.split('+'))   # 以加号为分隔符, 做为分隔符的字符会被删掉,所以这样可以直接把数字提取出来
print('1+2\n+3+4'.splitlines()) # 按照换行符去分割,转化为列表
print('LiFangCheng'.swapcase()) # 大写变小写, 小写变大写
print('li fang cheng'.title())  # 把每一个字符的首字母变成大写


