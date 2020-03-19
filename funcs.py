
"""
函数输入，参数x，默认是空链表的参数l
生成[0,x)的列表，计算其平方并插入到l的尾部，最后输出l

f(2)，计算0，1的平方，得到[0,1]
f(3,[3,2,1])，计算0，1，2的平方插入到[3,2,1]尾部，得到[3,2,1,0,1,4]
f(3)，计算0，1，2的平方，插入到对象l中，由于之前对象已经有了[0,1]，得到[0,1,0,1,4]
"""

def f(index,pow_append_list=None):
    i = 0
    pow_list = []
    while i<=index:
        pow_list.append(i**2)
        i+=1
    if type(pow_append_list) is not list:
        return pow_list
    else:
        pow_append_list.extend(pow_list)
        return pow_append_list
if __name__ == '__main__':
    print(f(3,[3,2,1]))
