'''
@Author: Baiy
@Date: 2018-11-04 21:23:06
@LastEditors: Baiy
@LastEditTime: 2018-11-04 21:29:35
@Email: yang01.bai@horizon.ai
@Company: Horizon Hobot
@Description: 
'''
from gevent import monkey
import gevent
import time,os,sys,random


#补丁来解决gevent所以延时的更换问题
monkey.patch_all()  # 将程序所有阻塞任务换位gevent的休眠操作


def current_work(workname,worktimes):
    for i in range(worktimes):
        print(workname,i)
        time.sleep(random.random())


gevent.joinall([
    gevent.spawn(current_work,"work1",3),
    gevent.spawn(current_work,"work2",4),
    gevent.spawn(current_work,"work3",5),
])


