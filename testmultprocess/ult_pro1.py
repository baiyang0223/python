"""多进程测试代码1-使用多进程来下载图片"""
from multiprocessing import Queue, Manager,Process,Pool
import requests
import time,os,random


obj_url=[
"https://rpic.douyucdn.cn/live-cover/appCovers/2018/10/30/5626336_20181030150100_small.jpg"
,
"https://rpic.douyucdn.cn/live-cover/appCovers/2018/09/24/2208656_20180924073440_small.jpg"
,
"https://rpic.douyucdn.cn/live-cover/appCovers/2018/11/01/5914251_20181101234641_small.jpg"
,
"https://rpic.douyucdn.cn/live-cover/appCovers/2018/09/03/2151454_20180903012818_small.jpg"
,"https://rpic.douyucdn.cn/live-cover/appCovers/2018/11/01/4930934_20181101081428_small.jpg"
]


def down_image(url,q,filename):
    u = requests.get(url)
    if u.status_code != 200:
        info =  "进程: " + str(os.getpid()) + " 下载图片:" + str(filename) + " 失败"
        q.put(info)
        return

    with open(filename,"wb") as f:
        f.write(u.content)  # request.text是str格式，content是bin格式

    info = "进程: " + str(os.getpid()) + " 下载图片:" + str(filename) + " 完成"
    q.put(info)


def main():
    """
    1.创建3个进程，每个进程都和主进程进行进程间通信
    2.每个进程去下载不同的图片，下载完成后告诉主进程
    """


    q = Queue()
    p0 = Process(target=down_image,args=(obj_url[0], q, "0.jpg"))
    p1 = Process(target=down_image,args=(obj_url[1], q, "1.jpg"))
    p2 = Process(target=down_image,args=(obj_url[2], q, "2.jpg"))
    p0.start()
    p1.start()
    p2.start()
    
    print(q.get())
    print(q.get())
    print(q.get())


if __name__ == "__main__":
    main()


"""
https://rpic.douyucdn.cn/live-cover/appCovers/2018/10/30/5626336_20181030150100_small.jpg

https://rpic.douyucdn.cn/live-cover/appCovers/2018/09/24/2208656_20180924073440_small.jpg

https://rpic.douyucdn.cn/live-cover/roomCover/2018/10/18/c40d706a911a84b7804ae9d43db5ca98_big.jpg

"""