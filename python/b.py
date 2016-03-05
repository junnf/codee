#!/usr/bin/env python
# encoding: utf-8

class A(object):

    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        if self._data < 0:
            raise ValueError("hi")
        else:
            return self._data

    @data.setter
    def data(self, value):
        self._data = value

class Descriptor(object):
    def __init__(self, value):
        self._value = value

    def __get__(self, instance, owner):
        return self._value ** 2

    def __set__(self, instance, value):
        print "fuck"
        instance._name = value

    def __delete__(self, instance):
        pass

class B(object):

    def __init__(self, name):
        self._name = name
    a = Descriptor(3)

class DD(object):
    X = Descriptor(3)

aa = B(11)
print aa.a
dd = DD()
print dd.X



