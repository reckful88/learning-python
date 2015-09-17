#####求一个列表中最大的元素######
def alist(n):
	a = n[0]
	for x in n:
		if x > a:
			a = x
		return a
