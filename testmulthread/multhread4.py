import threading
import time


g_num = 0
threadLock = threading.Lock()


def test1(temp):
    global g_num
    threadLock.acquire()
    print("%s-temp is %s-%d" % (threading.currentThread().name, str(temp),g_num))
    for i in range(temp):
        g_num += 1
    threadLock.release()
    print("%s-temp is %s-%d" % (threading.currentThread().name, str(temp),g_num))


def test2(temp):
    global g_num
    threadLock.acquire()
    print("%s-temp is %s-%d" % (threading.currentThread().name, str(temp),g_num))
    for i in range(temp):
        g_num += 1
    threadLock.release()
    print("%s-temp is %s-%d" % (threading.currentThread().name, str(temp),g_num))


def main():
    t1 = threading.Thread(target=test1, args=(10000000,),name="thread1")
    t2 = threading.Thread(target=test2, args=(10000000,),name="thread2")

    t1.start()
    t2.start()

    time.sleep(1)
    print("%s:g_num is %d" % (threading.current_thread().getName(),g_num ))
    print("t1 is alive-%d t2 is Alive-%d, main is Alive-%d" % 
        (t1.is_alive(),t2.is_alive(),threading.current_thread().is_alive() ))


if __name__ == "__main__":
    main()