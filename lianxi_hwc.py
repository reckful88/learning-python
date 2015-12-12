#-*- coding: utf-8 -*-
'''
g(x),判断一个字符串是否是回文串，类似：
'aba'
'abba'
'abcba' 
而 'abb' 这样的就不是
'''

def g(x):
    if x[:] == x[::-1]:
        return True
    else:
        return False


print g('aba')
print g('abb')
print g('abcba')
