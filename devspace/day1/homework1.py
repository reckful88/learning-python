#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng

'''
编写登陆接口

* 输入用户名密码
* 认证成功显示欢迎信息
* 输错三次后锁定
'''

_user = 'lfc'
_passwd = '123456'

with open('/Users/lifangcheng/ENV3.6/learning-python/devspace/day1/blacklist', 'r') as f:
    blacklist = f.read()

count = 0
while count < 3:
    username = input('请输入用户名：')
    passwd = input('请输入密码：')

    if username in blacklist:
        print("您的账号已被锁定，请联系管理员解锁.")
        break

    if username == _user and passwd == _passwd:
        print('登录成功，欢迎~')
        break
    else:
        print('登录失败，请检查用户名或密码是否正确！')
        count = count +1
else:
    print('尝试错误次数过多，账号已被锁定！')
    with open('/Users/lifangcheng/ENV3.6/learning-python/devspace/day1/blacklist', 'a') as f:
        f.write(username + '\n')
