"""
实现生成器的迭代
"""
def get_average():
    total = 0
    average = 0
    count = 0
    while True:
        new_num = yield average
        print("total",total)
        print("count",count)
        count +=1
        total += new_num
        average += total/count
def get_proxy():
    while True:
        yield from get_average()

cal = get_proxy()
print(next(cal))
print("-"*50)
print(cal.send(10))
print(cal.send(20))
print(cal.send(30))