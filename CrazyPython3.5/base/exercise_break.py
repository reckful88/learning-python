# -*- coding: utf-8 -*-

'''
在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：

n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')
'''

n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break
    print(n)
    n = n + 1
print('END')
