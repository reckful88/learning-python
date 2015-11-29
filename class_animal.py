class Aanimal(object):
	def run(self):
		print 'Animal is running...'
a=Aanimal()
a.run()
class Dog(Aanimal):
	def run(self):
		print 'HEY im a dog'

class Cat(Aanimal):
	pass

dog = Dog()
dog.run()

cat = Cat()
cat.run

print type(a)

print isinstance(dog,Aanimal)
print isinstance(dog,Dog)
print isinstance(cat,Dog)

def run_twice(Animal):     #定义一个run_twice，输出两次
	Animal.run()
	Animal.run()
print run_twice(a)

run_twice(Dog())
run_twice(Cat())

'''
有一个规则就是，不改变原有的代码，去添加新的显示内容
比如下面这个，新生成一个Horse，添加到新生成的run_twice函数中，
用run_twice继承Aanimal这个类，就可以输出了。
'''

class Horse(Aanimal):
    def run(self):
        print 'Horse is running ...'
run_twice(Horse())

#继承不要太多， 最多三层，太多反而不好
