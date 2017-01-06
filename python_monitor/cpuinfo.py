#!/usr/bin/env python
# coding:utf-8
# 获取CPU信息

#from __future__ import print_function
from collections import OrderedDict
#import pprint

def CPUinfo():
        """Return the infomation in /proc/CPUinfo
        as a dictionary the following format:
        CPU_info['proc0']={...}
        CPU_info['proc1']={...}
        """
        CPUinfo = OrderedDict()
        procinfo = OrderedDict()

        nprocs = 0
        with open('/proc/cpuinfo', 'rb') as f:
                for line in f:
                        if not line.strip():
                                # end of one processor
                                CPUinfo['proc{0}'.format(nprocs)] = procinfo
                                nprocs = nprocs + 1
                                # Reset
                                procinfo = OrderedDict()
                        else:
                                if len(line.split(':')) == 2:
                                        procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                                else:
                                        procinfo[line.split(':')[0].strip()] = ''
        return CPUinfo

if __name__ == '__main__':
        CPUinfo = CPUinfo()
        for processor in CPUinfo.keys():
                print CPUinfo[processor]['model name']