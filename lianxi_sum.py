sum = 0
for x in range(1,11):
	sum = sum + x
print sum


########1+2+3+.....+10################

'''
用递归的方法

def sums(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n + sums(n-1)

print sums(3)

'''
