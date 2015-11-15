#-*- coding:utf-8 -*-

'''
sort是正序排序，通过看sort？帮助，
得知后面加上一段即可倒序排列
'''

a = ['c','b','a']

a.sort()

a
#['a', 'b', 'c']
'''
a.sort?
Docstring:
    L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
    cmp(x, y) -> -1, 0, 1
    Type:      builtin_function_or_method
'''
a.sort(reverse=True)

a
#['c', 'b', 'a']
