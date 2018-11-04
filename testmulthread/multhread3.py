import threading
import time

number = 100
arr = [11,22]


def thread1():
    global number
    time.sleep(1)
    number += 1
    arr.append(33)
    print("thread1:number++ is %d-%s" % (number,arr))


def thread2():
    arr.append(44)
    print("thread2:number is %d-%s" % (number,arr))



if __name__ == "__main__":

    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)

    t1.start()
    t2.start()
    time.sleep(1)
    print("main thread  g_num is %d-%s" % (number,arr))