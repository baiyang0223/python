#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   testxshell.py
@Time    :   2018/11/24 10:32:59
@Author  :   BaiYang 
@Version :   1.0
@Contact :   yang01.bai@horizon.ai
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   交互式xshell
'''

import socket
import sys
import paramiko

has_termios = True
# windows does not have termios...
try:
    import termios
    import tty
    has_termios = True
except ImportError:
    has_termios = False


def interactive_shell(chan):
    if has_termios:
        posix_shell(chan)
    else:
        windows_shell(chan)

def posix_shell(chan):
    import select
    oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)
        while True:
            r, w, e = select.select([chan, sys.stdin], [], [])
            if chan in r:
                try:
                    x = chan.recv(1024)
                    if len(x) == 0:
                        print ('\r\n*** EOF\r\n',)
                        break
                    #x = x.decode("utf-8")
                    #print(">>>",type(x),x)
                    sys.stdout.write(x.decode("utf-8"))
                    sys.stdout.flush()
                except socket.timeout:
                    pass
            if sys.stdin in r:
                x = sys.stdin.read(1)
                if len(x) == 0:
                    break
                chan.send(x)
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)


# thanks to Mike Looijmans for this code
def windows_shell(chan):
    import threading
    sys.stdout.write("Line-buffered terminal emulation. Press F6 or ^Z to send EOF.\r\n\r\n")
    def writeall(sock):
        while True:
            data = sock.recv(256)
            if not data:
                sys.stdout.write('\r\n*** EOF ***\r\n\r\n')
                sys.stdout.flush()
                break
            sys.stdout.write(data.decode())
            sys.stdout.flush()
    writer = threading.Thread(target=writeall, args=(chan,))
    writer.start()
    try:
        while True:
            d = sys.stdin.read(1)
            if not d:
                break
            chan.send(d)
    except EOFError:
        # user hit ^Z or F6
        pass


def main():
    global has_termios

    #记录日志
    paramiko.util.log_to_file('./test')

    #建立ssh连接
    ssh=paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('127.0.0.1',port=22,username='baiy',password='123456',compress=True)

    #建立交互式shell连接
    channel=ssh.invoke_shell()

    #建立交互式管道
    interactive_shell(channel)

    #关闭连接
    channel.close()
    ssh.close()

if __name__ == "__main__":
    main()




#from uploadImg2linux import interactive
