#!/usr/bin/env python
# encoding: utf-8

class a(dict):
    def __getattribute__(self):
        print "AAAAAAAAAAA"

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError("aaa")

    def __setattr__(self, attr, value):
        self[attr] = value
        print self[attr]

class b(object):

    def __init__(self):
        pass

    def __getattr__(self, attr):
        if attr == "a":
            return 111
        else:
            raise AttributeError, attr

if __name__ == "__main__":
    a = b()
    a.a
