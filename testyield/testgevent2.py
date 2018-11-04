'''
@Author: Baiy
@Date: 2018-11-04 21:03:06
@LastEditors: Baiy
@LastEditTime: 2018-11-04 21:20:06
@Email: yang01.bai@horizon.ai
@Company: Horizon Hobot
@Description: 
'''
import gevent
import time,os,sys,random


def f(n1,n2,n3):
    print("start run f")
    for i in range(n3):
        print(gevent.getcurrent(),i,n1,n2,n3)
        gevent.sleep(0.1)


g1 = gevent.spawn(f,1,2,3)
g2 = gevent.spawn(f,4,5,6)
g3 = gevent.spawn(f,7,8,9)
print("start join func")
g1.join()
print("g1 finish")
g2.join()
print("g2 finish")
g3.join()
print("g3 finish")