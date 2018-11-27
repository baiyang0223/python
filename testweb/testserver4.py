'''
@Author: Baiy
@Date: 2018-11-14 13:10:35
@LastEditors: Baiy
@LastEditTime: 2018-11-18 08:00:11
@Email: yang01.bai@horizon.ai
@Company: Horizon Hobot
@Description: 模拟一个服务器，给web返回需要请求的页面
'''

import socket
import threading
from multiprocessing import  Process
import os,sys,random,time
import re


def exchange_2_client(tcp_s):
    client_info = tcp_s.getpeername()
    server_info = tcp_s.getsockname()
    print("client info:%s" % (str(client_info)))
    print("server info:%s" % (str(server_info)))

    """ 与客户端交互程序-每次交互完成必须关闭 ？"""
    print("==========================")
    send_data = None
    recv_data = tcp_s.recv(0x1024)
    if recv_data:
        recv_data = recv_data.decode("utf-8")
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


        tcp_s.close() #关闭后使得客户端不在菊花圈
      
    return 


def main():
    """写一个客户端，给服务器发送数据"""
    tcp_s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # availd address reused
    
    try:
        tcp_s.bind(("127.0.0.1", 9999))
    except OSError:
        print("端口号：9999已经呗占用，请关闭重试")
        tcp_s.close()
        return
    
    tcp_s.listen(128)

    s_info = tcp_s.getsockname()
    print("服务器：%s 等待客户端链接中..." % (str(s_info)))

    while True:
        client_sock,client_addr = tcp_s.accept()
        print("服务器-接收到来自%s的链接，准备收发数据" % (str(client_addr)))
        
        """ 使用多线程 """
        t1 = threading.Thread(target=exchange_2_client,name="exchange",args=(client_sock,))
        t1.start()

        """ 使用多进程（需要关闭当前进程的客户端句柄） """
        # p1 = Process(target=exchange_2_client,args=(client_sock,))
        # p1.start()
        # client_sock.close()  # 多进程会赋值socket描述符

        """ 基础的函数调用实现html服务 """
        #exchange_2_client(client_sock)  # 单任务直接函数调用即可。

    tcp_s.close()




if __name__ == "__main__":
    main()