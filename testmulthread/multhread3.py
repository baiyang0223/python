import threading
import time

number = 100
numbers = [11,22]

def change_number(val):
    """函数修改全局变量"""
    global number
    number = val


def change_number2():
    """因为numebers指向的数据可以修改"""
    numbers.append(3)


def thread1():
    global number
    time.sleep(1)
    number += 1
    print("thread1:number++ is %d" % number)


def thread2():
    print("thread2:number is %d" % number)



if __name__ == "__main__":
    print("num is %d" % number)
    change_number(3)
    print("num is %d" % number)
    change_number2()
    print(numbers)

    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)

    t1.start()
    t2.start()
    time.sleep(1)
    print("main thread  g_num is %d" % number)