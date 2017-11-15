LoggerServer Documentation
==========================

:doc:`logger_server.server` is an async TCP logging server base on tornado.ioloop,
which serve for logging.handlers.SocketHandler.

If you want get more information, please see `logging-cookbook. <https://docs.python.org/3/howto/logging-cookbook.html>`_

Module
======

.. toctree::
    :maxdepth: 2

    logger_server.server

Usage
======

1. Configure LoggerServer
-------------------------

Install `LoggerServer` by `pip`

.. code-block:: shell

    pip install logger_server

After `logger_server` package installed, you will got a command `logger-server`

`logger-server` options::

    usage: logger-server [-h] [-f CONF] [-p PORT] [--log LOG] [--when WHEN]
                         [--interval INTERVAL] [--backup BACKUP] [--fmt FMT]
                         [--datefmt DATEFMT]

    LoggerServer help documentation

    optional arguments:
      -h, --help            show this help message and exit
      -f CONF, --conf CONF  The config file path for LoggerServer. (default: None)
      -p PORT, --port PORT  LoggerServer port. (default: 9000)
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

Start `LoggerServer` on your server.

::

    $ logger_server

Output::

    > LoggerServer is binding on 0.0.0.0:9000

Release history
===============

Version 1.0.0, Nov 15 2017
--------------------------
* Release v1.0.0


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
