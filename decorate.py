#! /usr/bin/[ython
# -*- coding=utf-8 -*-
import time
import random
def hahah(name):
    def get_haha(func):
        def get_param(arg1):
            print("kskksks",name)
            func(arg1)
            print("sxsjksjhkhkjdhkjf")
        return get_param
    return get_haha

def timmer(func):
    def wrapper(name):
        start_time = time.time()
        print(start_time)
        func(name)
        stop_time = time.time()
        print(stop_time)
        print('run time is %s' % (stop_time - start_time))

    return wrapper


def auth(func):
    def deco(names):
        name = input('name: ')
        password = input('password: ')
        if name == 'c' and password == '123':
            print('login successful')
            func(names)  # wrapper()
            print("sssss")
        else:
            print('login err')

    return deco


@hahah(name="sss")
@auth  # index = auth(timmer(index))
@timmer  # index = timmer(index)
def index(name):
    time.sleep(3)
    print('welecome to index page',name)


index("sss")