#-*- coding:utf-8 -*-
#####求一个列表中最大的元素######
#def alist(n):
#	a = n[0]
#	for x in n:
#		if x > a:
#			a = x
#		return a


def maxmin(n):
    maxs = n[0]
    mins = n[0]
    for x in n:
        if maxs < x:
            maxs = x
        if maxs > x:
            mins = x
maxmin([1,2,3,4,5,6])
print max, mins

'''
In [26]: numbers = [4,3,6,1,7]

In [27]: maxs = numbers[0]

In [28]: mins = numbers[0]

In [29]: for x in numbers:
       ....:     if maxs > x:
              ....:         maxs = x
                 ....:     if mins < x:
                        ....:         mins = x                           ....:

In [30]: print maxs,mins
1 7
'''
