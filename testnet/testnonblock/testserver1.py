#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   testserver1.py
@Time    :   2018/11/20 09:07:20
@Author  :   BaiYang 
@Version :   1.0
@Contact :   yang01.bai@horizon.ai
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   测试tcp的非阻塞模式1：使用非阻塞单任务为多个客户端服务。
'''

import random,os,time,sys
import socket


def main():
    new_sock = None
    client_list = list()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # availd address reused
    server.bind(("",9998))
    server.listen(128)

    server.setblocking(False)
    while True:
        time.sleep(0.5)  #debug
        try:
            new_sock,_ = server.accept()
        except Exception as e:      # no client connect
            print("没有客户端链接......")
            pass
        else:
            print("有一个客户端链接(%s)......" % str(new_sock))
            new_sock.setblocking(False)
            client_list.append(new_sock)
            
        for client in client_list:
            try:
                content = client.recv(0x1024)
            except Exception as e:  # not read data
                print("---没有数据---")
                pass
            else:
                if content:
                    print(content.decode("utf-8")) # 处理数据
                else:    # 客户端关闭
                    print("客户端(%s)关闭<<<" % str(client))
                    client.close()
                    client_list.remove(client)


if __name__ == "__main__":
    main()