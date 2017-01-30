# -*- coding: utf-8 -*-

"""
list tuple 转为 dict
"""

# Tuple to List
mytuple = (1, 2, 3)
print (list(mytuple))


# List to Tuple
mylist = [1, 2, 3]
print (tuple(mylist))


# List to Dict
mylist2 = [('blue', 5), ('red', 3), ('yellow', 7)]
print (dict(mylist2))


# String to List
mystring = 'hello'
print (list(mystring))


# List to String
mylist3 = ['w', 'or',  'ld']
print (''.join(mylist3))
