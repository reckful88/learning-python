#!/usr/bin/env python
#encoding: utf-8
def sort(str):
    for x in range(1,len(str)):
        if str[x]<=str[x-1]:
            return False
    return True
