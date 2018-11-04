'''
@Author: Baiy
@Date: 2018-11-04 20:51:27
@LastEditors: Baiy
@LastEditTime: 2018-11-04 20:57:26
@Email: yang01.bai@horizon.ai
@Company: Horizon Hobot
@Description: file content
'''
from greenlet import greenlet
import time,os,sys,random

gr = list()

def test1():
    while True:
        print("-----A-----")
        gr[1].switch()
        time.sleep(1)


def test2():
    while True:
        print("-----B-----")
        gr[0].switch()
        time.sleep(1)


def main():
    gr.append(greenlet(test1))
    gr.append(greenlet(test2))
    
    #切换到第一个协程开始执行
    gr[0].switch()

    


if __name__ == "__main__":
    main()