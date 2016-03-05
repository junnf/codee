#!/usr/bin/python

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        print "class",cls
        print vars(cls)
        if '_inst' not in vars(cls):
            print vars(cls)
            cls._inst = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._inst

class A(Singleton):

    def __init__(self):
        pass

a = A()
b = A()
print id(a)
print id(b)
