#!/usr/bin/env python
#encoding: utf-8
class Employee(object):
	"所有员工的基类"
	empCount = 0
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1  
                '''
                每生成一个新变量，empCount 加 1， 触发条件为 init时 + 1
                也可以写成 Employee.empCount ＝ Employee.empCount ＋1
                '''

	def displayCount(self):
		print "Total Employee %d" % Employee.empCount # %d 十进制数字
	def displayEmployee(self):
		print "Name : ",self.name, ",Salary: ",self.salary

print "Employee._doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

'''
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入
模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了以个由所有父类组成的元组）
'''
