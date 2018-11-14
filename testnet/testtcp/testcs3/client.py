import socket


def exchange_2_server(tcp_s):
    """与服务器交互程序"""
    while True:
        send_data = input("客户端-输入文件名(q to quit):")
        if send_data == "q":
            break
        tcp_s.send(send_data.encode("utf-8"))
        recv_data = tcp_s.recv(0x4096)
        if not recv_data:
            print("客户端-服务器链接异常，请重试")
            break

        print("客户端收到 %s" % (recv_data.decode("utf-8")))
        with open (send_data, "wb") as f:
            f.write(recv_data)
        print("客户端-%s 下载完成" % (send_data))

    return 


def main():
    """写一个客户端，给服务器发送数据"""
    tcp_s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        tcp_s.connect(("10.31.112.198", 9999))
    except ConnectionRefusedError:
        print("服务器没开，稍后重试")
        tcp_s.close()
        return

    exchange_2_server(tcp_s)
    tcp_s.close()


if __name__ == "__main__":
    main()