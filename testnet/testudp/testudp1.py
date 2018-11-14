import socket

def udp_main():
    """创建udp套接字"""
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    """准备接收"""

    """使用udp套接字"""
    print("start to use udp_socket")

    """绑定端口(接收使用,发送不写也行，操作系统会随机分配一个),必须绑定自己的IP和端口"""
    local_addr = ("",8888) #IP地址不写 == INADDR_ANY
    udp_socket.bind(local_addr)

    """准备发送地址-元组（IP+端口）并发送数据"""
    udp_socket.sendto(b"Test net",("192.168.99.175",6666))
    udp_socket.sendto("hha".encode("utf-8"),("192.168.99.175",6666))
    """
    FAQ:
    TypeError: a bytes-like object is required, not 'str' 
    #发送数据必须为二进制,
    """
    while True:
        send_data = input("\n#>请输入要发送的数据:")
        if send_data == "exit":
            print("网络交互退出")
            break
        print("发送数据:%s"%(send_data))
        udp_socket.sendto(send_data.encode("gbk"),("192.168.99.175",6666))
        recv_data = udp_socket.recvfrom(0x1024) #param:接收长度
        print("接收数据:%s"%(str(recv_data)))  # (b'Test123', ('192.168.99.175', 6666))
        recv_msg = recv_data[0]  # 存放接收数据
        send_addr = recv_data[1]  # 存放发送方地址
        print("%s %s"%(str(send_addr),recv_msg.decode("gbk")))

    
    """关闭udp套接字"""
    udp_socket.close()


if __name__ == "__main__":
    udp_main()