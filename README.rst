LoggerServer
============

An async TCP logging server base on tornado.ioloop, which serve for logging.handlers.SocketHandler.

Introduce
---------

To solve `Python separate processes logging to same file <https://stackoverflow.com/questions/15096090/python-separate-processes-logging-to-same-file/47323076>`_.

Official description::

    Although logging is thread-safe, and logging to a single file from multiple threads in a single process is supported,
    logging to a single file from multiple processes is not supported, because there is no standard way to serialize access
    to a single file across multiple processes in Python. If you need to log to a single file from multiple processes, one
    way of doing this is to have all the processes log to a SocketHandler, and have a separate process which implements a
    socket server which reads from the socket and logs to file.

Reference: `logging cookbook <https://docs.python.org/3/howto/logging-cookbook.html#logging-to-a-single-file-from-multiple-processes>`_


``LoggerServer`` use ``tornado`` build a high-performance TCP logging server to slove this problem.


Documentation
-------------

See `LoggerServer Documentation <http://loggerserver.readthedocs.io/>`_.
