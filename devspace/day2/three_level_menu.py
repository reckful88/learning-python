#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng <shiwanyin199@gmail.com>

# data = {
#     '北京': {
#         '朝阳': {
#             '国贸': ['CBD', 'CCTV'],
#             '传媒大学': ['玲珑山', '珠江绿洲', '北花园']
#         },
#         '海淀': {
#             '中关村': ['ofo', '蚂蚁金服', '汽车之家'],
#             '圆明园': {'北京大学', '清华大学'},
#             '巴沟': {'万柳'}
#         },
#         '丰台': {
#             '公益西桥': ['角门东', '角门西']
#         },
#     },
#     '黑龙江': {
#         '哈尔滨': {},
#         '大庆': {},
#         '佳木斯': {}
#     },
#     '云南': {
#         '大理': {},
#         '普洱': {},
#         '昆明': {}
#     },
# }
#
# print(data)
#
# exit_flag = False
#
# while not exit_flag:
#     for i in data:
#         print(i)
#
#     choice = input('选择进入1>>:')
#     if choice in data:
#         while not exit_flag:
#             for j in data[choice]:
#                 print('\t', j)
#             choice2 = input(' 选择进入2>>:')
#             if choice2 in data[choice]:
#                 while not exit_flag:
#                     for x in data[choice][choice2]:
#                         print('\t', x)
#                     choice3 = input('选择进入3>>:')
#                     if choice3 in data[choice][choice2]:
#                         for z in data[choice][choice2][choice3]:
#                             print('\t\t', z)
#                         choice4 = input('最后一层,按 b 返回上一层')
#                         if choice4 == 'b':
#                             pass
#                         elif choice4 == 'q':
#                             exit_flag = True
#                 if choice2 == 'b':
#                     break
#                 elif choice2 == 'q':
#                     exit_flag = True


menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}


exit_flag = False
current_layer = menu

layers = [menu]

while not  exit_flag:
    for k in current_layer:
        print(k)
    choice = input(">>:").strip()
    if choice == "b":
        current_layer = layers[-1]
        #print("change to laster", current_layer)
        layers.pop()
    elif choice not  in current_layer:continue
    else:
        layers.append(current_layer)
        current_layer = current_layer[choice]