# 使用函数来实现多多任务的封装
import threading
import time


def sing():
    for i in range(5):
        print("{}---sing music---".format(threading.current_thread().name))
        time.sleep(1)


def dance():
    for i in range(10):
        print("{}---dance---".format(threading.current_thread().name))
        time.sleep(1)


def main():
    print("start:", end="")
    print(threading.enumerate())
    t1 = threading.Thread(target=sing,name="sing")
    t2 = threading.Thread(target=dance,name="dance")
   
    # 如果是run，则都是主线程去执行，threading.current_thread().name都是MainThread
    # t1.run()
    # t2.run()
    print("second:", end="")
    print(threading.enumerate())
    t1.start()
    t2.start()
    
    print("third:", end="")
    print(threading.enumerate())

    # 获取当前进程中线程数量
    while True:
        print(threading.enumerate())
        #print("当前线程数量为：%d" % (len(threading.enumerate())))

        if len(threading.enumerate()) <= 1:
            break
        time.sleep(1)

if __name__ == "__main__":
    main()