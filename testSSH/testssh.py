#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   testssh.py
@Time    :   2018/11/24 09:41:16
@Author  :   BaiYang 
@Version :   1.0
@Contact :   yang01.bai@horizon.ai
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   Test ssh and scp using python
'''


import paramiko
import os,time,sys,random


class x2Ssh(object):
    def __init__(self,server_address="127.0.0.1",server_port=22,username="baiy",passwd="123456"):
        self.service_address = server_address
        self.service_port = server_port
        self.username = username
        self.passwd = passwd
        self.res = None


    def x2_check_net(self,address):
        """ test netstat """
        ret = os.system("ping -c 1 " + address)
        return ret


    def x2_init_ssh(self):
        """ init ssh """
        ret = self.x2_check_net(self.service_address)
        if ret != 0:
            print("Network  %s  unreachable" % (self.service_address))
            return -1

        try:
            """创建ssh链接函数"""
            self.res = paramiko.SSHClient()
            self.res.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.res.connect(hostname=self.service_address, username = self.username,
                password = self.passwd,allow_agent=False,look_for_keys=False,
                port=self.service_port)
        except Exception as e:
            print("ssh %s@%s 链接失败:%s" % (self.username, self.service_address,e))
            return -1

        else:
            print("Ssh link is normal ")
            print(">>>"*8,"test pwd ")
            stdin,stdout,stderr = self.res.exec_command("pwd")
            print("test stdout: ", stdout.read().decode("utf-8"))
            print("test stderr: ", stderr.read().decode("utf-8"))

            # 测试如何远程执行超级用户命令-可行
            print(">>>"*8,"test sudo hwclock -r ")
            stdin,stdout,stderr = self.res.exec_command("sudo -s hwclock -r",get_pty=True)
            stdin.write("123456" + '\n')
            print("test stdout:  ", stdout.read().decode("utf-8"))
            print("test stderr:  ", stderr.read().decode("utf-8"))

            # 测试stderr和stdout是否都可以抓取到
            print(">>>"*8,"test ls >> /dev/stderr ")
            stdin,stdout,stderr = self.res.exec_command("ls >> /dev/stderr",get_pty=True)
            #stdin.write("123456" + '\n')
            print("测试标准输出[ls > /dev/stdout]: ", stdout.read().decode("utf-8"))
            print("测试错误输出[ls > /dev/stderr]: ", stderr.read().decode("utf-8"))
            #"""

            # 测试与远程交互
            print(">>>"*8,"test read -p ")
            stdin,stdout,stderr = self.res.exec_command("read -p \"nihao:\" val; echo $val",get_pty=True)
            stdin.write("buhao"+'\n')
            print("测试标准输出: ", stdout.read().decode("utf-8"))
            print("测试错误输出: ", stderr.read().decode("utf-8"))

        return 0


    def x2_exchange(self,cmd):
        """ exchange cmd and return result """
        _,stdout,stderr = self.res.exec_command(cmd)
        return stdout.read().decode("utf-8")


    def x2_deinit_ssh(self):
        self.res.close()


def main():
    s = x2Ssh()
    s.x2_init_ssh()
    s.x2_deinit_ssh()
    


if __name__ == "__main__":
    main()