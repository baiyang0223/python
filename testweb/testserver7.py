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
import select

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
        reponse_body = "没有你要的数据".encode("utf-8")
        reponse_header = "HTTP/1.1 404 Not found\r\n"
        reponse_header += "Content-Type: text/html;charset=utf-8\r\n"
        reponse_header += "Content-Length:%d\r\n" % len(reponse_body)
        reponse_header += "\r\n"

        tcp_s.send(reponse_header.encode("utf-8"))
        tcp_s.send(reponse_body)
    else:
        reponse_body = content

        reponse_header = "HTTP/1.1 200 OK\r\n"
        reponse_header += "Content-Type: text/html;charset=utf-8\r\n"
        reponse_header += "Content-Length:%d\r\n" % len(reponse_body)
        reponse_header += "\r\n"
        reponse = reponse_header.encode("utf-8") + reponse_body
        tcp_s.send(reponse)

    return


def main():
    fd_event_dict = dict()
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # availd address reused
    server.bind(("",9996))
    server.listen(128)
    server.setblocking(False)

    epl = select.epoll()  # 创建epoll对象
    epl.register(server.fileno(), select.EPOLLIN) # 加入到epoll监听表中,监听事件：输入

    while True:
        fd_event_list = epl.poll() #开始监听，可以设置超时时间
        #返回值 [(fd,event), ......] 一个元组的列表
        for fd,event in fd_event_list:
            if fd == server.fileno():   # accept
                new_sock,_ = server.accept()
                new_sock.setblocking(False)
                epl.register(new_sock.fileno(), select.EPOLLIN)
                # 这里一定要保存客户端的字典，描述fd->socket的匹配，因为epoll返回的是fd
                fd_event_dict[new_sock.fileno()] = new_sock

            elif event == select.POLLIN:
                content = fd_event_dict[fd].recv(0x1024)
                if content:
                    exchange_2_client(fd_event_dict[fd],content.decode("utf-8"))  # 处理数据
                else:    # 客户端关闭
                    print("客户端(%s)关闭<<<" % str(fd_event_dict[fd]))
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]



if __name__ == "__main__":
    main()