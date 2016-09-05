#!/usr/bin/env python
# encoding: utf-8

calls = 0
class tracer:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        global calls
        calls += 1
        print calls
        self.func(*args)

@tracer
def pam(a,b,c):
    print "111",a,b,c
@tracer
def spam(a,b,c):
    print "111",a,b,c

spam(1,2,3)
spam(1,2,3)
spam(1,2,3)
spam(1,2,3)
spam(1,2,3)
spam(111,2,3)
pam(1,2,3)
pam(1,2,3)
pam(1,2,3)
pam(1,2,3)
pam(1,2,3)
pam(111,2,3)

