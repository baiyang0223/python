from multiprocessing import Pool
from multiprocessing import Process
import time,os,random


def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号是%d" % (msg,os.getpid()))
    #random.random()随机生成0~1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg,"执行完毕,耗费时间%.2f" % (t_stop - t_start))

po = Pool(3)  #创建一个进程池，进程池中最多有三个进程 -》在第一次使用时创建进程,现在不创建

for i in range(0,10):
    #Pool().apply_async(调用函数,(传递参数元组))
    #每次循环将会用空闲出来的子进程去调用目标-目前最多启用三个，其余都在等待
    po.apply_async(worker, (i,))


print("---start---")
po.close()  # 关闭进程池，关闭后po不再接以后收新的请求，但之前的请求保留
po.join()   # 等待po中所有子进程执行完成，必须放在close之后
print("---end---")

