import threading
import os,time,random,sys

"""测试多线程的互斥访问以及全局变量、局部变量"""

class A():
    def __init__(self):
        self.num = 1
        self.arr = ["l1", "l2", "l3"]

    def __str__(self):
        return "A is : " + str(self.arr) + "->" + str(self.num)


g_num = 3
g_arr = [1,2,3]
g_dir = {"g_name":"baiy"}
a1 = A()
g_global1 = 400
g_global2 = 300


def func1(m1,m2,m3,m4,m5,m6,m7,m8):
    global g_global1
    g_global1 = -400
    g_global2 = -300  # 发现没有global声明的

    m1 = 300
    m2.append(4)
    m3["g_age"]=4
    m4.num = 4
    m5.num = -4
    m6 = -4
    m7.append(-4)
    m8["m_age"]=-4
    
    g_arr.append(5)
    g_dir["leng"]=5
    a1.arr.append(5)


def main():
    #
    a2 = A()
    num = 2
    arr = ["m1","m2"]
    mdir = {"m_name":"yanyan"}
    #t1 = threading.Thread(target=func1,args=(g_num,g_arr,g_dir,a1,a2,num,arr,mdir))
    #t1.start()
    #t1.join()
    func1(g_num,g_arr,g_dir,a1,a2,num,arr,mdir)
    print(g_num,g_arr,g_dir,a1,a2,num,arr,mdir)
    print(g_global1,g_global2)


if __name__ == "__main__":
    main()