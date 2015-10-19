class Student(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student object (name: %s)' % self.name
print Student('lfc')

################
#class student(object):
#	def __init__(self,name):
#		self.name = name
#print student('lfc')
#<__main__.student object at 0x7fd5085e0210>
#####################
###注释部分就是不加__str__的，直接打印出了变量在内存的位置，不好看。
##有很多用法，可以help(str)，多看看##########
