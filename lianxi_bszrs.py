#encoding: utf-8

'''
求出1000(n)以下3或者5的倍数的自然数的（和 或 乘积）
'''

def func(n):
    suma = 0
    sumb = 1
    for x in range(1,n):
        if x % 3 == 0 or x % 5 == 0:
            suma = suma + x
            sumb = sumb * x
    print suma,sumb
    
func(1000)
