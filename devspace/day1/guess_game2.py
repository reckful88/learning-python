#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng

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
