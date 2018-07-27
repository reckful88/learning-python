#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng <shiwanyin199@gmail.com>

'''
多级字典嵌套及操作
'''

# av_catalog = {
#     "欧美":{
#         "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
#         "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
#         "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
#         "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
#     },
#     "日韩":{
#         "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
#     },
#     "大陆":{
#         "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
#     }
# }
#
# av_catalog['大陆']['1024'][1] = 'aaa'
#
# print(av_catalog)


video_website = {
    "America": {
        'www.youtube.com': ['世界第一,需要翻墙', '油管'],
        'twitch.com': ['游戏直播', '大神云集', '国内观看速度感人'],
        'google.com': ['乱入一发谷歌']
    },
    "China": {
        'douyutv.com': ['国内直播平台一哥', '刷鱼丸礼物'],
        'panda.tv': ['老板是王思聪', '礼物是竹子'],
        'bilibili.com': 'B站!'
    }
}

print(video_website['China']['panda.tv'])
