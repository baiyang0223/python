import threading
import time

class Producer(threading.Thread):
    def run(self):
        global count
        while True:
            if con.acquire():
                if count > 300:
                    con.wait()
                else:
                    count = count+100
                    msg = self.name+' produce 100, count=' + str(count)
                    print(msg)
                    con.notify()
                con.release()
                time.sleep(1)


class Consumer(threading.Thread):
    def run(self):
        global count
        while True:
            if con.acquire():
                if count < 50:
                    con.wait()
                else:
                    count = count-10
                    msg = self.name+' consume 3, count='+str(count)
                    print(msg)
                    con.notify()
                con.release()
                time.sleep(0.1)


count = 200
con = threading.Condition()


def test():
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()
if __name__ == '__main__':
    test()