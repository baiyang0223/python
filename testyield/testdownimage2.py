from gevent import monkey
import gevent
import time,os,sys,random

#补丁来解决gevent所以延时的更换问题
monkey.patch_all()  # 将程序所有阻塞任务换位gevent的休眠操作

import urllib.request
from multiprocessing import  Queue


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
    u = urllib.request.urlopen(url)
    img_content = u.read()

    with open(filename,"wb") as f:
        f.write(img_content)

    info = "进程: " + str(os.getpid()) + " 下载图片:" + str(filename) + " 完成"
    q.put(info)


def main(): 
    q = Queue()
    gevent.joinall([
        gevent.spawn(down_image,obj_url[0],q,"0.jpg"),
        gevent.spawn(down_image,obj_url[1],q,"1.jpg"),
        gevent.spawn(down_image,obj_url[2],q,"2.jpg"),
    ])
    while not q.empty():
        print(q.get())


if __name__ == "__main__":
    main()