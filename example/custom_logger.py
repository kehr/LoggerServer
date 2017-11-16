#!/usr/bin/env python
#coding=utf-8
"""
@Project: LoggerServer
@Filename: custom_logger.py
@Author: Kehr <kehr.china@gmail.com>
@Created Date:   2017-11-16T10:57:24+08:00
@Last modified by:   Kehr
@Last modified time: 2017-11-16T10:58:12+08:00
@License: Apache License <http://www.apache.org/licenses/>
"""
import logging
import logging.handlers

# logger setting
logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)
# change localhost to your `logger-server` ip
socketHandler = logging.handlers.SocketHandler('localhost', 9000)
logger.addHandler(socketHandler)

logger.debug('The test logger is working!')
logger.info('The test logger is working!')
logger.warn('The test logger is working!')
logger.error('The test logger is working!')
logger.critical('The test logger is working!')
