#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng


'''
# 版本1

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
'''

'''
# 版本2

age_of_lfc = 26

count = 0
while count < 3:
    guess_age = int(input("guess a age: "))
    if guess_age == age_of_lfc:
        print("You are Right.")
        break
    elif guess_age > age_of_lfc:
        print("Too Old..")
    else:
        print("Too Young..")
    count = count +1
else:
    print("You geuss too many...")
'''

# 版本3

age_of_lfc = 26

for i in range(3):
    guess_age = int(input("guess a age: "))
    if guess_age == age_of_lfc:
        print("right")
        break
    elif guess_age > age_of_lfc:
        print("old")
    else:
        print("young")
else:
    print("try too many")
