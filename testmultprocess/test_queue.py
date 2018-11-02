from multiprocessing import Queue
from multiprocessing import Process
import time


def main():
    q = Queue(3)
    if not q.full():
        q.put("string")

    if not q.full():
        q.put([123])

    if not q.full():
        q.put({"name":"baiy"})
    
    if not q.empty():
        print("not empty")
    else:
        print("empty-size %d" % (q.qsize()))
        print(q.empty())
        print(q.full())

    while not q.empty():
        print(q.empty())
        print(q.full())
        print(q.qsize())
        print("current is :%s-left %d" % (str(q.get()), q.qsize()))


if __name__ == "__main__":
    main()

