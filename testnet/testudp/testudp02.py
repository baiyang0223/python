import socket


if __name__ == "__main__":
    udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 单纯发送，使用匿名端口
    udp_s.bind(("",8890))  # 如果不绑定，则使用匿名端口
    while True:
        s_data = input("input your message:")
        udp_s.sendto(s_data.encode("utf-8"),("127.0.0.1",8890))
        
