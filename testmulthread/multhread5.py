import threading
import time
import socket


dest_ip = "10.31.112.198"
dest_port = 9999
threadLock = threading.Lock()


def update_dest(dest_addr):
    global dest_ip
    global dest_port
    threadLock.acquire()
    dest_ip,dest_port = dest_addr
    threadLock.release()


def udp_snd(udp_sock,dest_addr):
    while True:
        send_data = input("输入要发送的数据： ")
        udp_sock.sendto(send_data.encode("utf-8"),dest_addr)


def udp_rcv(udp_sock):
    while True:
        recv_buf = udp_sock.recvfrom(0x1024)
        recv_data,peer_addr = recv_buf
        print("接收到来自%s的数据：%s" % (str(peer_addr),recv_data.decode("utf-8") ))


def main():
    udp_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    t1 = threading.Thread(target=udp_snd, args=(udp_sock,(dest_ip,dest_port)),name="udp_snd")
    t2 = threading.Thread(target=udp_rcv, args=(udp_sock,),name="udp_rcv")

    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
