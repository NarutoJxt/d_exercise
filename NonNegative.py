#! /usr/bin/[ython
# -*- coding=utf-8 -*-
"""
探究sub的1用法
"""
# import re
# o_str = "hsdjsadsadadasfas hello"
# o_repl = "o"
# s =re.sub("a",o_repl,o_str)
# print(s)
"""
random模块的使用
"""
import random
"""
shuffle 打乱对象元素的舒徐
"""
a = [1,2,3,4,5]
random.shuffle(a)
print(a)
#random 返回0-1之间的任意浮点数
s =random.random()
print(s)
#返回a-b之间的整数
a = random.randint(1,5)
print(a)
#返回p[a，b） or [a,b]之间的数
a = random.uniform(5,10)
print(a)
#返回序列中的一个元素
a = random.choice([1,2,3,4,5])
print(a)
#
random.choices()