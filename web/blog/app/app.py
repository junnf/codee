#!/usr/bin/env python
# encoding: utf-8

"""
@Author:junn
@Email:junnflow@gmail.com
@Date:2016-1-17
@Desc:blog
"""

import os.path
import logging
import torndb
import base64, uuid

import config

import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.options

from tornado.options import define, options

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
                (r'/login', BlogloginHandler),
                (r'/home', BlogHandler),
                (r'/register',BlogRegisterHandler),
                (r'/logout',BlogLogoutHandler),
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
        self.db = torndb.Connection('127.0.0.1','blog','root','ljn7168396123')


class BasicHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        #self.get_secure_cookie("user")
        return self.get_secure_cookie("user")

    @property
    def db(self):
        return self.application.db


class BlogHandler(BasicHandler):

    @tornado.web.authenticated
    def get(self):
        #  _get = self.db.query('select * from text')
        #  _text = _get[:5]
        #  self.render('index.html',user=self.current_user, text = _text)
        pass


class BlogRegisterHandler(BasicHandler):

    def get(self):
        self.render('register.html')

    def post(self):
        _username = self.get_argument('user')
        _password = self.get_argument('password')
        _get = self.db.query('select * from user where username = "{}"'.format(_username))
        if _get == []:
            self.db.execute("insert into user values('{}','{}');".format(_username, _password))
        else:
            self.write("<html><body><p>{} is used by other</p></body></html>".format(_username))

class BlogLogoutHandler(BasicHandler):

    def get(self):
        print self.get_current_user()
        self.clear_cookie("user")
        print self.get_current_user()


class BlogloginHandler(BasicHandler):

    def get(self):
        self.render('login.html')

    def post(self):
        login_user = self.get_argument('username')
        login_pass = self.get_argument('password')
        try:
            _get = self.db.query('select * from user where username = "%s"' % login_user)
            if _get[0]['password'] == login_pass:
                self.set_secure_cookie("user", login_user)
                self.redirect('/home')
        except:
            self.write("<html><body><p>your password is error</p></body></html>")


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
