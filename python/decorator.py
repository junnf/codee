#!/usr/bin/env python
# encoding: utf-8

def tracer(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print wrapper.calls
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@tracer
def a(x,y):
    print x + y

def x():
    x.y = 1
    print x.y
a(1,2)
a(1,2)
a(1,2)
a(1,2)
a(1,2)
x()
