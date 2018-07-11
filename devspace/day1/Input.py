#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng

username = input("YourName:")
password = input("YourPasswd:")

print(username, password)


# 格式化输出，三种不同的方式

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

info2 = '''
-------- info of {_name} -------
Name: {_name}
Age: {_age}
Job: {_job}
''' .format(_name = name,
            _age = age,
            _job = job)

print(info2)

info3 = '''
-------- info of {0} -------
Name: {0}
Age: {1}
Job: {2}
''' .format(name, name, age, job)

print(info3)
