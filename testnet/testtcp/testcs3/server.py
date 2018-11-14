import socket


def exchange_2_server(tcp_c):
    client_info = tcp_c.getpeername()
    server_info = tcp_c.getsockname()
    print("client info:%s" % (str(client_info)))
    print("server info:%s" % (str(server_info)))
   
    file_name = None

    """与客户端交互程序"""
    while True:
        send_data = None
        recv_data = tcp_c.recv(0x1024)
        if recv_data:
            print("客户端-收到服务器数据:%s" % (recv_data.decode("utf-8")))

            #  测试1：客户端接收数据时，服务器关闭了客户端描述符什么后果？-返回空数据
            #tcp_c.close()
            #break
            file_name = "/tmp/" + recv_data.decode("utf-8")
            try:
                f = open(file_name, "rb")
                send_data = f.read()
                tcp_c.send(send_data)
            except Exception as s:
                print("服务器-%s -%s" % (file_name,str(s)))
                #tcp_c.send(send_data) #  千万不能发送一个None类型的数据
                break
            
    return 


def main():
    """写一个客户端，给服务器发送数据"""
    tcp_s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        tcp_s.bind(("10.31.112.198", 9999))
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
        exchange_2_server(client_sock)
        print("服务器-客户端%s关闭，准备检测客户端链接。。。")
        client_sock.close()

    tcp_s.close()


if __name__ == "__main__":
    main()