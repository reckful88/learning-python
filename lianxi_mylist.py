#-*- coding: utf-8 -*-

'''
排序，从小往大
'''

def mylist(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue
    return alist

print mylist([7,2,4,5,3])

