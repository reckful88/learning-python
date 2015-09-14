#!/usr/bin/env python
#encoding: utf-8
class Parent:
	parentAttr = 100
	def __init__(self):
		self.__score = 20
		print "调用父类构造函数"
	def parentMethod(self):
		print "调用父类方法"
	def setAttr(self,attr):
		Parent.parentAttr = attr
		self.__score = attr
	def getAttr(self):
		print "父类属性:",Parent.parentAttr
		print "score: " , self.__score
a=Parent()
b=Parent()
a.setAttr(10)
b.getAttr()
class Child(Parent):
     def __init__(self):
         print "调用子类构造方法"
     def childMethod(self):
         print "调用子类方法 child method"
c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()



