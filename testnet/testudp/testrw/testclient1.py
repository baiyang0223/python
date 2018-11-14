import socket


def send_msg(udp_sock):
    """发送消息"""
    dest_ip = input("输入对方IP：")
    dest_port = int(input("输入对方端口："))
    send_data = input("输入你要发送的数据：")
    udp_sock.sendto(send_data.encode("utf-8"),(dest_ip,dest_port))


def recv_msg(udp_sock):
    """接收消息"""
    recv_buf = udp_sock.recvfrom(0x1024)
    recv_data = recv_buf[0]
    send_addr = recv_buf[1]
    print("接收到数据：%s-%s" % (recv_data.decode("utf-8"), str(send_addr)))


# 使用同一个套接字进行收发的服务端，先收后发
def udp_main():
    udp_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    udp_sock.bind(("", 9991))

    # 循环处理网络数据
    while True:
        #发送消息
        send_msg(udp_sock)

        # 接收消息并显示
        recv_msg(udp_sock)


if __name__ == "__main__":
    udp_main()