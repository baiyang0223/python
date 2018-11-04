from multiprocessing import Queue, Process
import time,os,sys


def download_from_web(q):
    """数据下载"""
    data = [ x for x in range(10000)] #模拟从网上下载数据
    print(os.getpid(),"开始下载数据")
    for temp in data:
        q.put(temp)
    print(os.getpid(),"已经下载完数据...")

def analysis_data(q):
    """数据分析"""
    waitting = list()

    """从队列中获取数据"""
    print(os.getpid(),"等待下载数据")
    while True:
        waitting.append(q.get())
        if q.empty():
            break
    print(os.getpid(),"已经处理完数据...%s" % (str(waitting)))


def main():
    """创建Queue，将Queue的引用传给多个进程"""
    q = Queue()  # 缺省大小为系统默认


    p1 = Process(target=download_from_web,args=(q,))
    p2 = Process(target=analysis_data,args=(q,))
    p1.start()
    p2.start()

if __name__ == "__main__":
    main()

