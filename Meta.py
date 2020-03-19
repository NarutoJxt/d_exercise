#! /usr/bin/[ython
# -*- coding=utf-8 -*-
"""
python元类基础
"""


# def upper_attr(future_class_name, future_class_parents, future_class_attr):
#     '''返回一个类对象，将属性都转为大写形式'''
#     #选择所有不以'__'开头的属性
#     attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
#     # 将它们转为大写形式
#     uppercase_attr = dict((name.upper(), value) for name, value in attrs)
#     #通过'type'来做类对象的创建
#     return type(future_class_name, future_class_parents, uppercase_attr)#返回一个类
#
# class Foo(object):
#     bar = 'bip'
#     __metaclass__ = upper_attr
#
# print(hasattr(Foo,"BAR"))
# class Foo(object):
#     def __init__(self, *args, **kwargs):
#         print("Foo __init__")
#     def __new__(cls, *args, **kwargs):
#         return object.__new__(Stranger, *args, **kwargs)
#
# class Stranger(object):
#     def __init__(self,name):
#         print("class Stranger's __init__ be called")
#         self.name = name
#
# foo = Foo("test")
# print(type(foo)) #<class '__main__.Stranger'>
# print(foo.name) #AttributeError: 'Stranger' object has no attribute 'name'

"""
实现单例模式
"""
# class Singleton(type):
# #     def __init__(self,*args,**kwargs):
# #         self._instance = None
# #         super(Singleton,self).__init__(*args,**kwargs)
# #     def __call__(self, *args, **kwargs):
# #         if self._instance is None:
# #             self._instance = super(Singleton,self).__call__(*args,**kwargs)
# #         return self._instance
# # class Foo(object):
# #     __metaclass__ = Singleton
# # f1 = Foo()
# # f2 = Foo()
# # print(f1)
# # print(f2)
class Singleton(type):
    def __init__(self, *args, **kwargs):
        print("__init__")
        self.__instance = None
        super(Singleton,self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("__call__")
        if self.__instance is None:
            self.__instance = super(Singleton,self).__call__(*args, **kwargs)
        return self.__instance


class Foo(object):
    __metaclass__ = Singleton #在代码执行到这里的时候，元类中的__new__方法和__init__方法其实已经被执行了，而不是在Foo实例化的时候执行。且仅会执行一次。


foo1 = Foo()
foo2 = Foo()
print(Foo.__dict__ ) #_Singleton__instance': <__main__.Foo object at 0x100c52f10> 存在一个私有属性来保存属性，而不会污染Foo类（其实还是会污染，只是无法直接通过__instance属性访问）

print(foo1 is foo2)  # True