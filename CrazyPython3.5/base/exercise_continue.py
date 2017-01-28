# -*- coding: utf-8 -*-

'''
在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。

n = 0
while n < 10:
    n = n + 1
    print(n)
'''

'''
上面的程序可以打印出1～10。但是，如果我们想只打印奇数，可以用continue语句跳过某
些循环：
'''

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
