#!/usr/bin/env python
# encoding: utf-8

"""
@Author:junn
@Email:junnflow@gmail.com
@Date:2016-1-17
@Desc:blog
"""

import os.path
#import logging
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
                (r'/', HomeHandler),
                (r'/login', BlogloginHandler),
                (r'/home', BlogHandler),
                (r'/register',BlogRegisterHandler),
                (r'/logout',BlogLogoutHandler),
                (r'/file',BlogUploadHandler),
                (r'.*',ErrorHandler),
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


class ErrorHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('base.html',page_title = "aaAAaa")

class BasicHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        #self.get_secure_cookie("user")
        return self.get_secure_cookie("user")

    @property
    def db(self):
        return self.application.db


class BlogUploadHandler(BasicHandler):
    """File Upload Test"""
    def get(self):
        self.render('fileloader.html')

    def post(self):
        upload_path=os.path.join(os.path.dirname(__file__),'files')
        print upload_path
        file_metas=self.request.files['file']
        for meta in file_metas:
            filename=meta['filename']
            filepath=os.path.join(upload_path,filename)
            with open(filepath,'wb') as up:
                up.write(meta['body'])
            self.write('finished!')


class HomeHandler(BasicHandler):

    """Docstring for HomeHandler. """

    def get(self):
        self.render('base.html')

    def post(self):
        """redirect to loginhandler"""
        self.render('login.html')


class BlogHandler(BasicHandler):

    @tornado.web.authenticated
    def get(self):
        print self.get_current_user()
        _t = self.db.query("select userid from user where username = '{}'".format(self.get_current_user()))
        _id = _t[0]['userid']
        _count = self.db.query('select count(*) from text where userid = {}'.format(_id))[0]['count(*)']
        if _count < 5 :
            if _count == 0:
                self.render('index.html')
                return
            _get = self.db.query('select textname, content, edittime from text where \
            userid = {}'.format(_id))
            self.render('index.html', article = _get)
        else:
            _get = self.db.query('select textname, content, edittime from text where \
            userid = {}'.format(_id))
            self.render('index.html', article = _get[:5])


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
        self.clear_cookie("user")


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
            #  self.write("<html><body><p>your password is error</p></body></html>")
            self.render('errorlogin.html')


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
