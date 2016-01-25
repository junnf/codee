#!/usr/bin/env python
# encoding: utf-8

"""
@Author:junn
@Email:junnflow@gmail.com
@Date:2016-1-17
@Desc:blog
"""

import os.path


import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.options

from tornado.options import define, options

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
                (r'/', TestHander),
                (r'/b',BHandler)
                ]

        settings = {
            "cookie_secret":"d2oEZ8T3TOqr1vhqDK2iIEilDgJ9OUO9lWyA+fGJ7tA=",
            "xsrf_cookies":True,
            "login_url":"/login",
            "template_path":os.path.join(os.path.dirname(__file__), "templates"),
            "static_path":os.path.join(os.path.dirname(__file__), "static"),
            "debug":True,
            }

        super(Application, self).__init__(handlers, **settings)


class BasicHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        #self.get_secure_cookie("user")
        return self.get_secure_cookie("user")

    @property
    def db(self):
        return self.application.db

class BHandler(BasicHandler):
    def get(self):
        self.render('b.html',text=['11','aa','cc'],header_text = "junningliu")


class TestHander(BasicHandler):
    def get(self):
        self.render('a.html')

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
