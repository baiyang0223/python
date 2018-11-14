import socket


def main():
    # 创建tcp套接字-买手机
    tcp_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 绑定tcp地址-办手机卡
    tcp_sock.bind(("",7890))

    # 创建socket套接字的默认属性是主动的，使用listen变为被动，这样就可以接收别人的链接了-手机设置为正常状态
    tcp_sock.listen(128)


    while True:
        # accept准备接收，等待客户端链接,返回元组：等号右边是个元组，等号左边是多个变量-拆包(元组个数和变量个数必须一致)
        # accept接收函数会阻塞到有新的链接连上，并返回新的套接字
        client_sock,client_addr = tcp_sock.accept()  # 返回一个新的套接字和客户端的地址，当客户端连上后返回
        print(client_sock)
        print(client_addr)
        while True:
            recv_data = client_sock.recv(0x1024)  #recv返回的仅仅只有数据，不需要对端地址
            print("收到数据：%s" % (recv_data.decode("utf-8")))
            if recv_data:
                client_sock.send("收到".encode("utf-8"))
            else:
                 break
        print("客户端服务完毕")
        client_sock.close()
    
    #close
    tcp_sock.close()

if __name__ == "__main__":
    main()