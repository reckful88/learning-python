#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng <shiwanyin199@gmail.com>

'''
程序：购物车程序

需求:
    1. 启动程序后，让用户输入工资，然后打印商品列表
    2. 允许用户根据商品编号购买商品
    3. 用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
    4. 可随时退出，退出时，打印已购买商品和余额
'''

product_list = [
    ('iphoneX', 9800),
    ('MacBook Pro', 19800),
    ('iPad', 4500),
    ('Apple Watch 3', 2900),
    ('AirPods', 1000)
]

salary = input('请输入您的工资: ')

shopping_list = []

if salary.isdigit():       # 判断是否为整数
    salary = int(salary)
    while True:
        for index, item in enumerate(product_list):     #  通过列表的角标作为商品编号
            #print(product_list.index(item), item)
            print(index, item)
        user_choice = input('根据商品编号选择您要购买的商品, 按 q 退出>>>: ')
        if user_choice.isdigit():   # 判断输入的是否是数字
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:    # 输入的商品编号不能超过范围
                p_item = product_list[user_choice]      # 通过角标取到商品
                if p_item[1] <= salary:     # 判断商品价格小于用户工资
                    shopping_list.append(p_item)
                    salary = salary - p_item[1]
                    print('商品: %s 已经放入了您的购物车中, 您的当前工资余额为: \033[32;1m%s\033[0m' % (p_item, salary))
                else:
                    print('\033[31;1m 您的余额只剩[%s], 无法继续购买\033[0m' % salary)
            else:
                print('商品编号 [%s] 不存在.' % user_choice)
        elif user_choice == 'q':
            print('------ 已购买清单 ------')
            for p in shopping_list:
                print(p)
            print('您的当前余额为: ', salary)
            exit()
        else:
            print('错误的选项, 退出请输入 q ')