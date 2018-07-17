#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng

'''
编写登陆接口

* 输入用户名密码
* 认证成功显示欢迎信息
* 输错三次后锁定
'''


with open('/Users/lifangcheng/ENV3.6/learning-python/devspace/day1/userpasswd', 'r') as f1:
    userpasswd = f1.readlines()

with open('/Users/lifangcheng/ENV3.6/learning-python/devspace/day1/blacklist', 'r') as f2:
    blacklist = f2.readlines()

for x in range(3):
    username = input('请输入用户名：')
    passwd = input('请输入密码：')

    flag1 = False
    for j in blacklist:
        j = j.strip()
        if username == j:
            print("您的账号已被锁定，请联系管理员解锁.")
            flag1 = True
            break
    if flag1 == True:
        break

    flag = False
    for i in userpasswd:
        i = i.strip()
        a, b = i.split(":")
        if a == username and b == passwd:
            print("登陆成功，欢迎 ~")
            flag = True
            break
    if flag == True:
        break

    else:
        print('登录失败，请检查用户名或密码是否正确！')

else:
    print('尝试错误次数过多，账号已被锁定！')
    with open('/Users/lifangcheng/ENV3.6/learning-python/devspace/day1/blacklist', 'a') as f2:
        f2.write(username + '\n')
