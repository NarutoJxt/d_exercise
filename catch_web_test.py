#! /usr/bin/[ython
# -*- coding=utf-8 -*-
def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3 # 女性福音 :-)
        return method_to_decorate(self, lie)
    return wrapper

class Lucy(object):
    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print("I am %s, what did you think?" % (self.age + lie))

l = Lucy()
l.sayYourAge(-3)
