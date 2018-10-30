import threading
import time
import socket


def test(number):
    total = number
    while number:
        print("线程%s-%d..." % (threading.current_thread().name, total-number+1))
        time.sleep(1)
        number -= 1


def main():
    udp_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    t1 = threading.Thread(target=test,args=(10,),name="test")
    t1.setDaemon(True)

    t1.start()
    #因为t1设置主线程为守护线程，此时主线程不能结束，否则t1会立即结束
    while t1.is_alive():
        print("t1 is alive, sleep...")
        time.sleep(1)
    print("t1 is close, quit")

if __name__ == "__main__":
    main()
