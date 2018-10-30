# 使用类来实现多多任务的封装
import threading
import time


class myThread(threading.Thread):
    def run(self):
        print("Thread name:%s" % self.name)
        self.longin()
        self.register()

    def longin(self):
        print("Thread name:%s-login" % self.name)

    def register(self):
        print("Thread name:%s-register" % self.name)


if __name__ == "__main__":
    t = myThread()
    t.start()