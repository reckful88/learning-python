def func(n):
	sum = 1
	for x in range(1,n+1):
		sum = sum * x
	return sum

########## 求 n！ 也就是 1*2 * 3 * 4.. *n 这个式子的值##########



'''
用递归的方式
高级用法

def f(N):
    if N == 1:
        return 1
    else:
        return N * f(N-1)

print f(3)

'''


