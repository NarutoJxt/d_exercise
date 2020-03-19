
"""
实现线程池
"""
def func(data_param):
    def func_outer(func_param):
        print(type(func_param))
        def func_inner(*args):
            if data_param == 'man':
                print("Type is man")
                func_param()
            else:
                print("Type is woman")

        return func_inner

    return func_outer


@func # 等价于func_execute=func(func_execute)
def func_man():
    print("I am func_man")


@func("woman")
def func_woman():
    print("I am func_man")


"""
如果需要返回函数的话，带参数的装饰器就要写三层内嵌函数
带参数的装饰器具体执行过程分为两步：首先执行func("man"),不管中间过程，func函数返回的是函数func_outer的内存地址，
此时就变成了@func_outer,按照不带参数的装饰器的调用过程，此时func_outer将函数func_man的名称当做是参数执行func_outer
里面的函数func_inner()。另外，现在func_inner里不仅有func_man,还有fun本身所携带的参数'man'
"""

if __name__ == '__main__':
    func_man()
    func_woman()