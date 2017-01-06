#!/usr/bin/env python
# coding:utf-8
# 系统负载监测


import os

def load_stat():
        loadavg = {}
        with open('/proc/loadavg', 'rb') as f:
                con = f.read().split()
        loadavg['lavg_1'] = con[0]
        loadavg['lavg_5'] = con[1]
        loadavg['lavg_15'] = con[2]
        loadavg['nr'] = con[3]
        loadavg['last_pid'] = con[4]
        return loadavg
print "loading", load_stat()['lavg_15']