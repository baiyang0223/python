"""多进程测试代码1-使用进程池来下载图片"""
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
    num = 0
    q = Manager().Queue()
    po = Pool(2)
    for temp in obj_url:
        po.apply_async(down_image,(temp,q,str(num)+".jpgs"))
        num += 1
 
    print("main(" + str(os.getpid()) + "):start waiting...")
    po.close()
    po.join()
    print("main(" + str(os.getpid()) + "):stop waiting...")
    while not q.empty():
        print(q.get())


if __name__ == "__main__":
    main()
