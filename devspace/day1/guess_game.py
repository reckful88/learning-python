#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng


age_of_lfc = 26

count = 0
while True:
    if count == 3:  # 尝试3次
        break
    guess_age = int(input("guess age: "))
    if guess_age == age_of_lfc:
        print("You are right!")
        break
    elif guess_age < age_of_lfc:
        print("too young")
    else:
        print("too old")
    count = count +1