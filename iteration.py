"""
实现类的迭代
"""
# class A():
#     def __init__(self,n):
#         self.idx = 0
#         self.n = n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.idx < self.n:
#             val,self.idx = self.idx,self.idx+1
#             return val
#         else:
#             raise StopIteration
# a = A(5)
# for i in a:
#     print(i)

"""
迭代器实现fib数列
"""
class Fib():
    def __init__(self):
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        return self.a
f = Fib()
count = 0
for i in f:
    if(count<50):
        print(i)
        count+=1
    else:
        break
