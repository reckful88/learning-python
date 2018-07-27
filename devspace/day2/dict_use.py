#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng <shiwanyin199@gmail.com>


info = {
    'name1': 'lifangcheng',
    'name2': 'reckful',
    'name3': 'lfc'
}

'''
查找
'''
print(info['name1'])
print(info.get('name2'))  # 安全的查找,有就显示,没有就返回空,不报错
print('name73' in info)  # 判断一个 key 是否在字典中,在就返回 True

'''
修改
'''

info['name1'] = 'Lifangcheng'
print(info['name1'])

'''
增加
'''
info['name4'] = 'abcdd'  # 如果key 存在就修改,不存在就创建
info['name5'] = 'aaaa'
print(info)

'''
删除
'''
# del info['name4']
# info.pop('name5')
# print(info)
#
