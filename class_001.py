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

''' 以下这些调用方法 是实例化 
上面都是在初始化，定制模版 '''

tom = Student('tom',99, 17)
lily = Student('lily',87, 19)

tom.change_name('lifangcheng')
print tom.get_name()

tom.change_name('xiaotom')
print tom.get_name()

'''
调用方法

tom.get_score()
lily.get_name()
print tom.name   ＃这种调用方法就是隐藏，只看结果，不看过程
print tom.__name ＃这句则会报错，因为__name是私有的，无法直接调用，
                    多用这种私有方法，保留隐私，不让外界直接调用

'''

