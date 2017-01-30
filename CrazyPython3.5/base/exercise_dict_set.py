# -*- coding: utf-8 -*-


"""
dict使用键-值（key-value）存储，具有极快的查找速度。
"""

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print (d)
print (d['Michael'])


"""
把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
"""

d['Adam'] = 67
print(d)
print(d['Adam'])


"""
通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
"""

print (d.get('Thomas'))
print (d.get('Thomas', -1))


"""
要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
"""

print (d)
d.pop('Bob')
print (d)


"""
set
"""

s = set([1, 2, 2, 3, 3, 4, 5])
print (s)


"""
通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
"""

s.add(6)
print (s)


"""
通过remove(key)方法可以删除元素：
"""

s.remove(4)
print(s)
