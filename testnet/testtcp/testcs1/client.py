import socket


def main():
    # 1.创建tcp套接字
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.链接服务器
    #server_ip = input("请输入服务器IP： ")
    #server_port = int(input("请输入服务器端口号： "))
    server_ip = "127.0.0.1"
    server_port= 7890
    server_addr = (server_ip, server_port)
    # bind只是为了让当前程序有一个端口，这里不用bind系统也会默认分配一个,客户端一般不绑定
    # tcp_sock.bind(("",10000))  
    tcp_sock.connect(server_addr)

    while True:
        # 3.发送数据、接收数据
        send_data = input("请输入要发送数据： ")
        tcp_sock.send(send_data.encode("utf-8"))

        recv_buf = tcp_sock.recv(0x1024)
        #print(recv_buf)
        #print(type(recv_buf))  #recv 二进制数据
        print("接收数据：%s" % (recv_buf.decode("utf-8")))

    # 4.关闭tcp套接字
    tcp_sock.close()

if __name__ == "__main__":
    main()