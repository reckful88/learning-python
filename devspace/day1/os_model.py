#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lifangcheng

import os

cmd_ps = os.system("ps -ef") # os.system() 只执行命令,不保存结果
print(cmd_ps)

cmd_ps2 = os.popen('ps -ef').read() # 执行命令,读取
print(cmd_ps2)

os.mkdir('test_dir') # 创建目录

