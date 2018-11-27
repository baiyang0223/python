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
import re

def exchange_2_client(tcp_s,recv_data):
    client_info = tcp_s.getpeername()
    server_info = tcp_s.getsockname()
    print("client info:%s" % (str(client_info)))
    print("server info:%s" % (str(server_info)))

    """ 与客户端交互程序-每次交互完成必须关闭 ？"""
    print("==========================")
    send_data = None
    print("客户端-收到服务器数据:%s" % (recv_data))


    """ 使用目录操作 """
    #req_file = recv_data.split()
    # # 去掉路径的根目录号
    # req_file[1] = re.match("/(.*)",req_file[1]).group(1)
    # file_name = os.path.join(os.getcwd(),"testhtml")
    # file_name = os.path.join(file_name,req_file[1]) #经过测试，发现需要去掉"/"

    """ 使用正则表达式获取路径"""
    req_lines = recv_data.splitlines()
    print(req_lines)
    #get/post/put/del
    filename = re.match(r"([^/]+)/([^ ]*)",req_lines[0])
    if filename:
        filename = filename.group(2)
        if filename == "":
            filename = "./index.html"
        filename = os.path.join("/home/baiy/workspace/testcode/python/testweb/testhtml",\
            filename)
    try:
        f = open(filename,"rb")
        content = f.read()            
        f.close()
    except:
        send_data = "HTTP/1.1 404 Not found\r\n"
        send_data += "\r\n"
        tcp_s.send(send_data.encode("utf-8"))
        tcp_s.send("没有你要的数据".encode("utf-8"))
    else:
        send_data = "HTTP/1.1 200 OK\r\n"
        send_data += "\r\n"
        tcp_s.send(send_data.encode("utf-8"))
        tcp_s.send(content)


    #tcp_s.close() #关闭后使得客户端不在菊花圈
      
    return


def main():
    client_list = list()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # availd address reused
    server.bind(("",9999))
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
            print("dump client:" ,client.getpeername())

        for client in client_list:

            try:
                content = client.recv(0x1024)
            except Exception as e:  # not read data
                print("---没有数据---[%d]" % len(client_list))
                pass
            else:
                if content:
                    #print(content.decode("utf-8")) # 处理数据
                    exchange_2_client(client,content.decode("utf-8"))
                    client.close()
                    client_list.remove(client)
                else:    # 客户端关闭
                    print("客户端(%s)关闭<<<" % str(client))
                    client.close()
                    client_list.remove(client)


if __name__ == "__main__":
    main()