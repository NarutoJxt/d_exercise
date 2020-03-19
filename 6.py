#! /usr/bin/[ython
# -*- coding=utf-8 -*-

"""
1、请尽可能列举python列表的成员方法，并给出列表操作的答案：
（1） a=[1, 2, 3, 4, 5], a[::2]=?, a[-2:] = ?


"""
"""
（2）一行代码实现对列表a中的偶数位置的元素进行加3后求和？
"""
# a = [1,2,3,4,5]
# def func(x):
#     return  a.index(x)%2==0
# print(list(map(lambda x:x+3,list(filter(func,a)))))
"""
（3）将列表a的元素顺序打乱，再对a进行排序得到列表b，然后把a和b按元素顺序构造一个字典d。
"""
import random
a = [1,2,3,4,5,6]
random.shuffle(a)
b = sorted(a)
print(dict(zip(a,b)))