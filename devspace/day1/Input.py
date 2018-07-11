#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng

username = input("YourName:")
password = input("YourPasswd:")

print(username, password)


# 格式化输出

name = input("YourName:")
age = int(input("YourAge:"))
print(type(age))
job = input("YourJob")

info = '''
--------- info of %s ----------
Name: %s
Age: %d
Job: %s
''' % (name, name, age, job)

print(info)
