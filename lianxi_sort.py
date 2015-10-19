#!/usr/bin/env python
#encoding: utf-8
def sort(str):
    for x in range(1,len(str)):
        if str[x]<=str[x-1]:
            return False
    return True


#######假设 len(str)为7,该函数判断的是当前位和下一位的大小，判断到str[6]的时候其实也就已经判断完了,当判断到str[6]的时候，说明前面都没有问题，这时候返回True即可.如果前面有问题，肯定早就返回False了.#######################


##测试一个字符串的顺序，顺序正确如‘abcde’则返回True，如果顺序错误如‘qwerty’则返回False##
