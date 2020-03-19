#! /usr/bin/[ython
# -*- coding=utf-8 -*-
def gen_func(index):
    for i in range(index):
        yield i
for i in gen_func(50000000000):
    print(i)