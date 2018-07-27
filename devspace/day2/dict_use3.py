#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng <shiwanyin199@gmail.com>

info = {
    'name1': 'lifangcheng',
    'name2': 'reckful',
    'name3': 'lfc'
}

print(info.values())  # 打印出所有除了 key 以外的值

print(info.keys())  # 打印出所有 key

'''
setdefault
'''

info.setdefault('new', {'www.baidu.com': [1, 2]})  # 如果取不到就新建一个 key, 并赋值
print(info)
info.setdefault('name1', {'www.baidu.com': [1, 2]})  # 在字典里取指定的值, 如果能取到, 就把取到的这个值返回
print(info)

'''
update

把两个字典合并, 把有交叉的 key 进行合并更新,没有交叉的新 key 就进行创建
'''

b = {
    'name1': 'lifaaaaaaa',
    1: 2,
    3: 4
}

print(b)
info.update(b)
print(info)

'''
iterm
'''

print(info.items())  # 把字典转成列表

'''
fromkeys

初始化一个新的字典, 并赋值
'''
new_dict = dict.fromkeys([6, 7, 8], "test")
new_dict2 = dict.fromkeys([6, 7, 8])
print(new_dict)
print(new_dict2)

new_dict3 = dict.