#!/usr/bin/env python
#coding=utf-8
"""
@Project: LoggerServer
@Filename: root_logger.py
@Author: Kehr <kehr.china@gmail.com>
@Created Date:   2017-11-16T10:56:10+08:00
@Last modified by:   Kehr
@Last modified time: 2017-11-16T12:00:13+08:00
@License: Apache License <http://www.apache.org/licenses/LICENSE-2.0>
"""
import logging
import logging.handlers

# root logger setting
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# change localhost to your `logger-server` ip
socketHandler = logging.handlers.SocketHandler('localhost', 9000)
logger.addHandler(socketHandler)

# use root logger
logging.debug('The root logger is working!')
logging.info('The root logger is working!')
logging.warn('The root logger is working!')
logging.error('The root logger is working!')
logging.critical('The root logger is working!')

# unsetted logger inherit the settings of root logger by default.
logger = logging.getLogger('default_logger')
logger.debug('The default logger is working!')
logger.info('The default logger is working!')
logger.warn('The default logger is working!')
logger.error('The default logger is working!')
logger.critical('The default logger is working!')
