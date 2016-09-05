#!/usr/bin/env python
# encoding: utf-8

def single(cls, *args, **kwargs):
    instance = {}
    def _single(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
            print instance
        return instance[cls]
    return _single

@single
class MyClass(object):
    """Docstring for MyClassMyClass. """

    def __init__(self,word):
        """TODO: to be defined1. """

a = MyClass(1)

