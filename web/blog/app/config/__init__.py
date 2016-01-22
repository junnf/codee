#!/usr/bin/env python
# encoding: utf-8
import tornado.ioloop
import logging
import tornado.options

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)
#not define mysql

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='../log/blog.log',
                    filemode ='w')
