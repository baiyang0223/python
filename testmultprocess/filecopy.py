from multiprocessing import Queue, Manager,Process,Pool
import time,os,random


def copy_file(ipc, src_f, filename, dst_f):
    #print("模拟拷贝: 目录:%s 文件名:%s->目标:%s" % (src_f,filename,dst_f))
    #print(src_f + "/" + filename)
    #print(dst_f + "/" + filename)
    src_fd = open(src_f + "/" + filename, "rb")
    content = src_fd.read()
    src_fd.close()

    dst_fd = open(dst_f + "/" + filename, "wb")
    dst_fd.write(content)
    dst_fd.close()

    ipc.put(filename)


def main():
    finish = 0
    """实现文件拷贝"""
    # 获取用户指定目录或者文件
    src_f = input("输入要拷贝的目录或者文件? ")

    # 在当前目录下创建拷贝的副本文件
    try:
        dst_f = src_f + "-副本"
        os.mkdir(dst_f)
    except:
        pass

    # 获取目录下所有文件名
    all_f = os.listdir(src_f)
    #print(all_f)

    # 创建进程池
    po = Pool(3)  #创建一个进程池，进程池中最多有三个进程

    #　实现进度－进程间通信
    ipc = Manager().Queue()

    for name in all_f:
        po.apply_async(copy_file, args = (ipc,src_f, name, dst_f))
    
    # 主线程休眠
    print("---start---")
    po.close()  # 关闭进程池，关闭后po不再接以后收新的请求，但之前的请求保留
    #po.join()   # 等待po中所有子进程执行完成，必须放在close之后
    while True:
        finish += 1
        filename = ipc.get()
        #print("%s copy finish - %d/%d" % (filename,finish,len(all_f)))
        print("\r进度：%.2f%%" % (finish * 100 / len(all_f)), end="")
        if(finish >= len(all_f)):
            break

    print("\n---end---")  


if __name__ == "__main__":
    main()