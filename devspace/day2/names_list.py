#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng <shiwanyin199@gmail.com>

names =  ['lifangcheng', 'lfc', 'reckful', 'haha', 'jack', 'tom']
print(names)
print(names[0], names[2])

'''
切片是从左往右开始查.   查
'''
print(names[1:3])   # 切片, 取第二个元素到第四个元素
print(names[-1])    # 取一个列表最后的一个元素
print(names[-2:])   # 取最后两个值
print(names[:3])    # 取前三个元素
print(names.index('haha'))  # 查一个值在列表中所在的位置
print(names[names.index('haha')])
print(names.count('lfc'))   # 统计一个列表里面有多少个 'lfc'


'''
插入.    增
'''
names.append('zxc') # 追加一个元素到列表的末尾
print(names)
names.insert(2, 'insert')   # 将一个元素, 插入到指定位置
# names.insert(1, ['aaa','bb','cc'])
print(names)


'''
改变一个元素.   改
'''
print(names)
names[5] = 'jackson'    # 更改指定位置的元素
print(names)


'''
删除一个元素
'''
print(names)
names.remove('insert')  # 删除指定元素
print(names)
names.pop() # 默认删除位置在最后一个的元素
print(names)
names.pop(5)    # 删除位置在第五的元素
print(names)


'''
翻转列表
'''

print(names)
names.reverse()
# a = names[::-1]
print(names)


'''
对无序的列表进行排序, 按照 特殊符号 -> 数字 -> 大写字母 -> 小写字母 
'''
print(names)
names.sort()
print(names)


'''
将另外一个列表 合并到一个列表中
'''

names2 = [1, 2, 3, 4]
names.extend(names2)
del names2  # 删掉一个变量
print(names)