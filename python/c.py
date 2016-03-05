#!/usr/bin/env python
# encoding: utf-8

class a(object):
    def __init__(self,data):
        self.data = data

    def __getattribute__(self, name):
        print "fuck"

    def __str__(self):
        return "xxxxxxxx"

z = a("xyz")
print z
print z.dataa
