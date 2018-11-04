'''
@Author: Baiy
@Date: 2018-11-04 17:10:52
@LastEditors: Baiy
@LastEditTime: 2018-11-04 20:37:32
@Email: yang01.bai@horizon.ai
@Company: Horizon Hobot
@Description: 使用协程来实现并发
'''
import os, sys, random, time

def func1():
    while True:
        print("----func1---")
        yield
        time.sleep(0.1)


def func2():
    while True:
        print("----func2---")
        yield
        time.sleep(0.1) 


if __name__ == "__main__":
    f1 = func1()
    f2 = func2()
    
    while True:
        next(f1)
        next(f2)