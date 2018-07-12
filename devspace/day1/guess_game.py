#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng


age_of_lfc = 26

guess_age = int(input("guess age: "))

if guess_age == age_of_lfc:
    print("You are right!")
elif guess_age < age_of_lfc:
    print("too young")
else:
    print("too old")
