#!/usr/bin/env python
#coding=utf-8
"""
@Project: LoggerServer
@Filename: server.py
@Author: Kehr <kehr.china@gmail.com>
@Created Date:   2017-11-14T19:20:37+08:00
@Last modified time: 2017-11-16T14:50:51+08:00
@License: Apache License <http://www.apache.org/licenses/LICENSE-2.0>
"""
import os
import socket
import pickle
import struct
import functools
import logging
import logging.handlers
import datetime
import argparse
import json
import tornado.ioloop

from tornado import gen
from tornado.log import LogFormatter
from tornado.tcpserver import TCPServer
from tornado.iostream import StreamClosedError

version = __version__ = '1.0.2'

DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
DEFAULT_LOG_FORMAT = '[%(levelname)1.1s %(asctime)s %(ip)s %(name)s %(module)s:%(lineno)d] %(message)s'


class AttrDict(dict):
    """Attribute dict

    Make ``dict`` value can be accessed by attribute::

        from logger_server import AttrDict

        people = AttrDict({'name':'Joe', 'age': 23})
        print people.name
        print people.age

    """
    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        return self[key]


class LoggerFormatter(LogFormatter):
    """format """
    def formatTime(self, record, datefmt=None):
        """Rewrite default `formatTime` to support `%f`

        :arg logging.LogRecord record:  ``logging.LogRecord`` object which
            Contains all the information pertinent to the event being logged.
        :arg datefmt:  Datetime format string.
        """
        ct = datetime.datetime.fromtimestamp(record.created)
        datefmt = DEFAULT_DATE_FORMAT if not datefmt else datefmt
        return ct.strftime(datefmt)


class LoggerStreamHandler(TCPServer):
    """A stream handler for TCP connection.

    Reference: `tornado.tcpserver.TCPServer <http://www.tornadoweb.org/en/stable/tcpserver.html#tornado.tcpserver.TCPServer>`_
    """
    def __init__(self, *args, **kwargs):
        super(LoggerStreamHandler, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger('LoggerServer')

    @gen.coroutine
    def handle_stream(self, stream, address):
        """Reslove Socket stream data.

        :arg stream: scoket stream
        :arg tuple address: client resquest ip and port ``(ip, port)``
        """
        self.request_ip, self.request_port = address
        while True:
            try:
                chunk = yield stream.read_bytes(4)
                if len(chunk) < 4:
                    break
                slen = struct.unpack('>L', chunk)[0]
                chunk = yield stream.read_bytes(slen)
                while len(chunk) < slen:
                    chunk += yield stream.read_bytes(slen - len(chunk))
            except StreamClosedError:
                break
            data = pickle.loads(chunk)
            self.handleLogRecord(logging.makeLogRecord(data), address)

    def handleLogRecord(self, record, address):
        """Config the decoded `record`

        This will add ``ip`` and ``port`` param by ``logging.Filter``. You can
        add them into logging format::

            [%(levelname)1.1s %(asctime)s %(ip)s %(port)s %(name)s %(module)s:%(lineno)d] %(message)s

        :arg logging.LogRecord record:  ``logging.LogRecord`` object which
            Contains all the information pertinent to the event being logged.
        :arg tuple address: client resquest ip and port `(ip, port)`
        """
        class ContextFilter(logging.Filter):
            """为日志增加额外信息"""
            def filter(self, record):
                record.ip, record.port = address
                return True
        logger = logging.getLogger(record.name)
        logger.addFilter(ContextFilter())
        logger.handle(record)


class LoggerServer(object):
    """A logging server serve for ``logging.handlers.SocketHandler``"""
    def __init__(self):
        self.options = AttrDict()
        self.init_config_options()
        self._init_logger()
        self.ioloop = tornado.ioloop.IOLoop.current()

    def start(self):
        """Start LoggerServer"""
        if self.options.conf:
            print '> Use config: {}'.format(self.options.conf)
        print '> LoggerServer is binding on 0.0.0.0:{}'.format(self.options.port)
        LoggerStreamHandler().listen(self.options.port)
        self.ioloop.start()

    def _init_logger(self):
        """init global logger"""
        logger = logging.getLogger()
        channel = logging.handlers.TimedRotatingFileHandler(
                                filename=self.options.log,
                                when=self.options.when,
                                interval=self.options.interval,
                                backupCount=self.options.backup)
        channel.setFormatter(LoggerFormatter(fmt=self.options.fmt, datefmt=self.options.datefmt, color=False))
        logger.addHandler(channel)

    def init_config_options(self):
        """Initialize `logger-server` config.

        All settings will be merged in ``self.options``
        """
        command = self._parse_command()
        self.options.update(command.__dict__)
        if command.conf:
            self.options.update(self._parse_config_file(command.conf))

    def _parse_config_file(self, path):
        """Parses the config file at the given path"""
        with open(os.path.abspath(path)) as f:
            return json.load(f, encoding='utf-8')

    def _parse_command(self):
        """Parses the command args"""
        p = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            description='LoggerServer help documentation')
        p.add_argument('-f', '--conf', required=False, default=None,
                        help='The config file path for LoggerServer.')

        p.add_argument('-p', '--port', required=False, type=int, default=9000,
                        help='LoggerServer port.')

        p.add_argument('--log', required=False, default='./logserver.log',
                        help='The log output file.')

        p.add_argument('--when', required=False, default='midnight',
                        help=('specify the type of TimedRotatingFileHandler interval.'
                        "other options:('S', 'M', 'H', 'D', 'W0'-'W6')"))

        p.add_argument('--interval', required=False, type=int, default=1,
                        help='The interval value of timed rotating.')

        p.add_argument('--backup', required=False, type=int, default=14,
                        help='Number of log files to keep.')

        p.add_argument('--fmt', required=False, default=DEFAULT_LOG_FORMAT,
                        help='The log output formatter of logging.')

        p.add_argument('--datefmt', required=False, default=DEFAULT_DATE_FORMAT,
                        help='The log output date formatter of logging.')

        return p.parse_args()


def main():
    """LoggerServer Entry"""
    LoggerServer().start()


if __name__ == '__main__':
    main()
