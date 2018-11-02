from collections import Iterable, Iterator
import os,sys,random,time

class Fibonacci():
    def __init__(self,collect_allnum=0):
        self.arr = list()
        self.cursor = 0
        self.collect_allnum = collect_allnum
        self.num1 = 0
        self.num2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor < self.collect_allnum:
            ret = self.num1
            self.num1,self.num2 = self.num2, self.num1+self.num2
            #print("ret:",ret)
            #time.sleep(1)
            self.cursor += 1
            return ret
        else:
            self.cursor = 0
            raise StopIteration
            

# 不使用迭代器,生成斐波那契数列的前20个数据
num1 = 0
num2 = 1

arr = list()
for i in range(20):
    arr.append(num1)
    #会先算等号右边的，此时等号右边依次从左到右开始算，生成一个元组 (num2, num1+num2)，然后等号就是拆分元组
    num1,num2 = num2,num1+num2

print("使用列表：",arr)

#sys.exit(0)
fibo = Fibonacci(20)
print("使用迭代器：",end="")
for num in fibo:
    print(num,end=" ")
print()






