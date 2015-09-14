#######类  下划线不对称 就是私有的，反之 是共有的，self代表其本身#########

class Student(object):
	def __init__(self,name,score,age):
		self.__name = name
		self.__score = score
		self.__age = age
	def get_score(self):
		return self.__score

	def print_score(self):
		print '%s:%s' % (self.__name,self.__score)
	def _print_ok(self):
		print "im ok"
	def change_name(self,new_name):
		self.__name = new_name
	def get_name(self):
		return self.__name

tom = Student('tom',99, 17)
lily = Student('lily',87, 19)

tom.change_name('lifangcheng')
print tom.get_name()

tom.change_name('xiaotom')
print tom.get_name()
