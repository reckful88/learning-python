#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng

# 错误尝试达到3次后，询问是否继续，只要输入的不是 N 或者 n 就可以继续。

age_of_lfc = 26

count = 0

while count < 3:
    guess_age = int(input("guess a age:"))
    if guess_age == age_of_lfc:
        print("right.")
        break
    elif guess_age > age_of_lfc:
        print("old.")
    else:
        print("young.")
    count = count +1
    if count == 3:
        go_on = input("do you want go on ?")
        if go_on != 'n' and go_on != 'N':
            count = 0
