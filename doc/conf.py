#!/usr/bin/env python
#coding=utf-8
"""
@Project: LoggerServer
@Filename: conf.py
@Author: Kehr <kehr.china@gmail.com>
@Created Date:   2017-11-15T19:22:45+08:00
@Last modified time: 2017-11-15T22:34:40+08:00
@License: Apache License <http://www.apache.org/licenses/>
"""
import os
import sys
sys.path.insert(0, os.path.abspath(".."))
from logger_server import server

master_doc = "index"

project = "LoggerServer"
copyright = "2017, kehr.china@gmail.com"

version = release = server.version

extensions = ["sphinx.ext.autodoc", "sphinx.ext.coverage", "sphinx.ext.viewcode"]

primary_domain = 'py'
default_role = 'py:obj'

autodoc_member_order = "bysource"
autoclass_content = "both"

coverage_skip_undoc_in_source = True

html_last_updated_fmt = '%Y/%m/%d %H:%M:%S'
