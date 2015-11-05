#-*- coding:utf-8 -*-
sum_a = 0
sum_b = 0
for x in range(1,101):
	if x % 2 == 0:
		sum_a = sum_a + x
	else:
		sum_b = sum_b + x
print sum_a
print sum_b
print sum_a - sum_b
#求偶数和 and  奇数和 以及 之间的差###
