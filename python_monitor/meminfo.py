#!/usr/bin/env python
# coding:utf-8
# 内存信息获取


from collections import OrderedDict

def meminfo():
        """Return the infomation in /proc/meminfo
        as a dictionary
        """
        meminfo = OrderedDict()

        with open('/proc/meminfo') as f:
                for line in f:
                        meminfo[line.split(':')[0]] = line.split(':')[1].strip()
        return meminfo

if __name__ == '__main__':
        # print meminfo()
        meminfo = meminfo()
        print "Total memory: {0}".format(meminfo['MemTotal'])
        print "Free memory: {0}".format(meminfo['MemFree'])
