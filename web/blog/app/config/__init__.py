#!/usr/bin/env python
# encoding: utf-8
import tornado.ioloop
import tornado.options

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)
#  define("mysql_host", default="127.0.0.1", help="blog database host")
#  define("mysql_database", default="blog", help="blog database name")
#  define("mysql_user", default="root", help="blog database user")
#  define("mysql_password", default="ljn7168396123", help="blog database password")
