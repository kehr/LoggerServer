#!/usr/bin/env python
#coding=utf-8
"""
@Project: LoggerServer
@Filename: test_logger.py
@Author: Kehr <kehr.china@gmail.com>
@Created Date:   2017-11-14T20:06:48+08:00
@Last modified time: 2017-11-16T12:00:35+08:00
@License: Apache License <http://www.apache.org/licenses/LICENSE-2.0>
"""
import unittest
import logging
import logging.handlers

root = logging.getLogger()
root.setLevel(logging.DEBUG)
socketHandler = logging.handlers.SocketHandler('localhost', 9000)
root.addHandler(socketHandler)

class TestLogger(unittest.TestCase):
    """Test LoggerServer"""
    def test_root_logger(self):
        """test root logger"""
        logging.debug('I am feeling good!')
        logging.info('I am feeling good!')
        logging.warn('I am feeling good!')
        logging.error('I am feeling good!')
        logging.critical('I am feeling good!')

    def test_custom_logger(self):
        """test custom logger"""
        logger = logging.getLogger('custom')
        logger.debug('I am feeling very good!')
        logger.info('I am feeling very good!')
        logger.warn('I am feeling very good!')
        logger.error('I am feeling very good!')
        logger.critical('I am feeling very good!')

    def test_chinese_logger(self):
        """test chinese logger"""
        logger = logging.getLogger('chinese')
        logger.debug('呦呦切克闹，你有free style么？')
        logger.info('呦呦切克闹，你有free style么？')
        logger.warn('呦呦切克闹，你有free style么？')
        logger.error('呦呦切克闹，你有free style么？')
        logger.critical('呦呦切克闹，你有free style么？')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLogger)
    unittest.TextTestRunner(verbosity=2).run(suite)
