#! /usr/bin/[ython
# -*- coding=utf-8 -*-
"""
探究property的用法
"""
class A:
    def __init__(self,name,passwrd):
        self.name = name
        self.password = passwrd
    @property
    def haha(self):
        return self.name
    @haha.setter
    def name(self,value):
        if value>999:
            raise ValueError("ssss")
        else:
            self._name = value
a = A(36,123)
a.name = 55555