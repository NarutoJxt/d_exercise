#! /usr/bin/[ython
# -*- coding=utf-8 -*-
import time
from functools import wraps

def my_log(my_print):
    def out(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            my_print(name=kwargs['name'], inp=kwargs['inp'])
            result = func(*args, **kwargs)
            return result

        return wrap

    return out


def my_print(*args, **kwargs):
    #     %Y  Year with century as a decimal number.
    #     %m  Month as a decimal number [01,12].
    #     %d  Day of the month as a decimal number [01,31].
    #     %H  Hour (24-hour clock) as a decimal number [00,23].
    #     %M  Minute as a decimal number [00,59].
    #     %S  Second as a decimal number [00,61].
    current_day_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    current_time_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
    with open(f'{current_day_time}操作日志.txt', 'a', encoding='utf-8') as f:
        f.write(f'{current_time_time}:操作人：{kwargs["name"]},操作方式：{kwargs["inp"]}\n')


@my_log(my_print=my_print)
def operation(*, name, inp):
    print('操作成功！')
if __name__ == '__main__':
    operation(name="jjaja",inp="r")