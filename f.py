def f(n):
	if n == 0 or n == 1:
		return 1
	if n > 1:
		return f(n-1) + f(n-2)



##############
#f(0) = 1
#f(1) =1 
#f(2) = f(1) + f(0)
#…
#f(n) = f(n-1) + f(n-2)
#求 f(n) 这个函数该如何定义。
######
