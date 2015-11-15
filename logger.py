#!/usr/bin/env python
#encoding: utf-8
import logging

logger = logging.getLogger('app')		#生成日志对象
log_file = logging.FileHandler('/var/tmp/app.log')	#设置日志记录文件
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')	#设置日志记录形式
log_file.setFormatter(formatter)	#配置
logger.addHandler(log_file)		#配置
logger.setLevel(logging.WARNING)	#设置日志记录等级

logger.error('We have a problem')
logger.info('Not log this info')

