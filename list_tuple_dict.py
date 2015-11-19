# -*- coding: utf-8 -*-

'''
list tuple 转为dict类型 互相转换
'''
mytuple = (1,2,3)
print list(mytuple)     #Tuple to list

mylist = [1,2,3]
print tuple(mylist)     #List to tuple


mylist2 = [('blue',5),('red',3),('yellow',7)]
print dict(mylist2)     #List to dict


mystring = 'hello'
print list(mystring)    #String to list


mylist3 = ['w','or','ld']
print ''.join(mylist3)  #List to string


