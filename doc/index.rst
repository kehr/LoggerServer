LoggerServer Documentation
==========================

:doc:`logger_server.server` is an async TCP logging server base on `tornado.ioloop <http://www.tornadoweb.org/en/stable/ioloop.html>`_,
which serve for `logging.handlers.SocketHandler <https://docs.python.org/2/library/logging.handlers.html?highlight=sockethandler#sockethandler>`_.

More information, see `logging-cookbook <https://docs.python.org/3/howto/logging-cookbook.html>`_.

Usage
=====

1. Install
----------

Install `LoggerServer` by `pip`

.. code-block:: shell

    pip install logger_server


2. Configuration
----------------

After `logger_server` package installed, you will got a command `logger-server`

`logger-server` options::

    $ logger_server -h
    usage: logger-server [-h] [-f CONF] [-p PORT] [--log LOG] [--when WHEN]
                         [--interval INTERVAL] [--backup BACKUP] [--fmt FMT]
                         [--datefmt DATEFMT]

    LoggerServer help documentation

    optional arguments:
      -h, --help            show this help message and exit
      -f CONF, --conf CONF  The config file path for LoggerServer. (default: None)
      -p PORT, --port PORT  LoggerServer port. (default: 9876)
      --log LOG             The log output file. (default: ./logserver.log)
      --when WHEN           specify the type of TimedRotatingFileHandler
                            interval.other options:('S', 'M', 'H', 'D', 'W0'-'W6')
                            (default: midnight)
      --interval INTERVAL   The interval value of timed rotating. (default: 1)
      --backup BACKUP       Number of log files to keep. (default: 14)
      --fmt FMT             The log output formatter of logging. (default:
                            [%(levelname)1.1s %(asctime)s %(ip)s %(name)s
                            %(module)s:%(lineno)d] %(message)s)
      --datefmt DATEFMT     The log output date formatter of logging. (default:
                            %Y-%m-%d %H:%M:%S.%f)
      --detached            Running on detached mode. (default: False)

Use param `-f` to specify a config file for `logger-server`.
`logserver.conf.template <https://github.com/kehr/LoggerServer/blob/master/logger_server/conf/logserver.conf.template>`_ is a configuration template.

.. versionadded:: 1.0.3

    Use param `--detached` to set `logger-server` runnning as daemon.

.. warning::

    By default, the config file setttings over command settings.

**Start LoggerServer** ::

    $ logger_server

Output::

    > LoggerServer is binding on 0.0.0.0:9876

.. note::

    ``logger-server`` bind on port `9876` by default. if this port is not avalible, use param `-p` specify a new port.


3. Hello word
-------------

After start `logger-server`, now you can write your logging code, like below:

**Example1**  use root logger::

    import logging
    import logging.handlers

    # root logger setting
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # change localhost to your `logger-server` ip
    socketHandler = logging.handlers.SocketHandler('localhost', 9876)
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

Output::

    [D 2017-11-16 11:13:19.700965 127.0.0.1 root root_logger:23] The root logger is working!
    [I 2017-11-16 11:13:19.702461 127.0.0.1 root root_logger:24] The root logger is working!
    [W 2017-11-16 11:13:19.702587 127.0.0.1 root root_logger:25] The root logger is working!
    [E 2017-11-16 11:13:19.702661 127.0.0.1 root root_logger:26] The root logger is working!
    [C 2017-11-16 11:13:19.702759 127.0.0.1 root root_logger:27] The root logger is working!
    [D 2017-11-16 11:13:19.702844 127.0.0.1 default_logger root_logger:31] The default logger is working!
    [I 2017-11-16 11:13:19.702919 127.0.0.1 default_logger root_logger:32] The default logger is working!
    [W 2017-11-16 11:13:19.702979 127.0.0.1 default_logger root_logger:33] The default logger is working!
    [E 2017-11-16 11:13:19.703068 127.0.0.1 default_logger root_logger:34] The default logger is working!
    [C 2017-11-16 11:13:19.703124 127.0.0.1 default_logger root_logger:35] The default logger is working!

Get this example code `root_logger.py <https://github.com/kehr/LoggerServer/blob/master/example/root_logger.py>`_.

**Example2** use custom logger::

    import logging
    import logging.handlers

    # logger setting
    logger = logging.getLogger('test')
    logger.setLevel(logging.DEBUG)
    # change localhost to your `logger-server` ip
    socketHandler = logging.handlers.SocketHandler('localhost', 9876)
    logger.addHandler(socketHandler)

    logger.debug('The test logger is working!')
    logger.info('The test logger is working!')
    logger.warn('The test logger is working!')
    logger.error('The test logger is working!')
    logger.critical('The test logger is working!')

Output::

    [D 2017-11-16 11:19:48.623884 127.0.0.1 test custom_logger:22] The test logger is working!
    [I 2017-11-16 11:19:48.625533 127.0.0.1 test custom_logger:23] The test logger is working!
    [W 2017-11-16 11:19:48.625658 127.0.0.1 test custom_logger:24] The test logger is working!
    [E 2017-11-16 11:19:48.625739 127.0.0.1 test custom_logger:25] The test logger is working!
    [C 2017-11-16 11:19:48.625821 127.0.0.1 test custom_logger:26] The test logger is working!

Get this example code `custom_logger.py <https://github.com/kehr/LoggerServer/blob/master/example/custom_logger.py>`_.

Module
======

.. toctree::
    :maxdepth: 2

    logger_server.server


Release history
===============

Version 1.0.3, Nov 16 2017
--------------------------
* Add ``--detached`` param.

Version 1.0.0, Nov 15 2017
--------------------------
* Release v1.0.0
