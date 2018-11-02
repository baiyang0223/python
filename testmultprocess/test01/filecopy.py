from multiprocessing import Pool
from multiprocessing import Process
import time,os,random


def main():
    """实现文件拷贝"""
    # 获取用户指定目录或者文件
    src_f = input("输入要拷贝的目录或者文件?")

    # 在当前目录下创建拷贝的副本文件
    dst_f = mkdir(src_f + "[副本]")

    #获取目录下所有文件名
    all_f = os.listdir(src_f)
    print(all_f)


if __name__ == "__main__":
    main()