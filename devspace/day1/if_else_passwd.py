#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng

# 密文密码

import getpass

_username = "lfc"
_passwd = 123

username = input("your user name is :")
passwd = int(getpass.getpass("your password is :"))
print(type(passwd))

# print(username, passwd)

if _username == username and _passwd == passwd:
    print("Welcome 用户：{name} login..." .format(name=username))
else:
    print("Not login, error username or passwd !!")
