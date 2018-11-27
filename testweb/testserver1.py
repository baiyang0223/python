'''
@Author: Baiy
@Date: 2018-11-14 13:10:35
@LastEditors: Baiy
@LastEditTime: 2018-11-18 06:35:21
@Email: yang01.bai@horizon.ai
@Company: Horizon Hobot
@Description: 模拟一个服务器，给所有web返回一样的数据
'''

import socket
import threading
import os,sys,random,time

def exchange_2_client(tcp_s):
    client_info = tcp_s.getpeername()
    server_info = tcp_s.getsockname()
    print("client info:%s" % (str(client_info)))
    print("server info:%s" % (str(server_info)))

    """与客户端交互程序"""
    print("=="*8)
    send_data = None
    recv_data = tcp_s.recv(0x1024)
    if recv_data:
        print("客户端-收到服务器数据:%s" % (recv_data.decode("utf-8")))
        send_data = "HTTP/1.1 200 OK\r\n"
        send_data += "\r\n"
        send_data += "<h1>This is a test web</h1>\r\n"
        print("服务器-回复客户端的数据:",send_data)
        tcp_s.send(send_data.encode("utf-8")) #二进制发送数据
        tcp_s.close()
    else:
        print("客户端%s关闭链接" % (str(client_info)) )
        tcp_s.close()

    return 


def main():
    """写一个客户端，给服务器发送数据"""
    tcp_s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
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
        
        # t1 = threading.Thread(target=exchange_2_client,name="exchange",args=(client_sock,))
        # t1.start()
        exchange_2_client(client_sock)

    tcp_s.close()




if __name__ == "__main__":
    main()