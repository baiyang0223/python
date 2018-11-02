import threading
import time
import multiprocessing

numbers = 100

def test01():
    global numbers
    while True:
        print("%s(%d) - numbers is %d" % (multiprocessing.current_process().name, 
                multiprocessing.current_process().pid,numbers))
        numbers += 1
        time.sleep(1)


def test02():
    global numbers
    while True:
        print("%s(%d) - numbers is %d" % (multiprocessing.current_process().name, 
                multiprocessing.current_process().pid,numbers))
        numbers += 1
        time.sleep(1)


def main():
    """多进程操作"""
    p1 = multiprocessing.Process(target=test01, name="test01")
    p2 = multiprocessing.Process(target=test02, name="test02")
    p1.start()
    p2.start()

    while True:
        print("%s(%d) - numbers is %d" % (multiprocessing.current_process().name,
                 multiprocessing.current_process().pid,numbers))
        time.sleep(1)


if __name__ == "__main__":
    main()