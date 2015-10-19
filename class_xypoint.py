#encoding: utf-8
import math

class point(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def get_x(self):
		return self.__x
	def get_y(self):
		return self.__y
	def print_xy(self,other):
		print math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)

a = point(1,2)
b = point(3,4)
a.print_xy(b)

##############定义类 Point.  来描述平面上的一个点(x,y).  可以求两点直线距离。 ############
