#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   testscp.py
@Time    :   2018/11/24 09:57:58
@Author  :   BaiYang 
@Version :   1.0
@Contact :   yang01.bai@horizon.ai
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''


import paramiko,os,sys,time


port = 22


def ssh_scp_put(ip,port,user,password,local_file,remote_file):
    """ 上传文件 """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, user, password)
    a = ssh.exec_command('date')
    stdin, stdout, stderr = a
    print(stdout.read())
    sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    sftp = ssh.open_sftp()
    sftp.put(local_file, remote_file)

def ssh_scp_get(ip, port, user, password, remote_file, local_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, user, password)
    a = ssh.exec_command('date')
    stdin, stdout, stderr = a
    print(stdout.read())
    sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    sftp = ssh.open_sftp()
    sftp.get(remote_file, local_file)



#ip = input("请输入远端主机的IP地址：")
#password = input("请输入远端主机的密码：")

while True:
    print('''
    -------欢迎使用 scp software--------
    上传文件请输入  [ 1 ]:
    下载文件请输入  [ 2 ]:
    退出SCP请输入   [ q ]:
    ------------------------------------
    ''')
    choice = input("请输入 [ ]")
    if choice == "1":
        local_file = input("请输入本地文件的绝对路径：")
        remote_file = input("请输入文件上传的绝对路径：")
        #ssh_scp_put(ip,port,baiy,password,local_file,remote_file)
        ssh_scp_put("127.0.0.1",22,"baiy","123456",local_file,remote_file)
    elif choice == "2":
        remote_file = input("请输入远端文件的绝对路径：")
        local_file = input("请输入要放到本地的绝对路径：")
        ssh_scp_get("127.0.0.1",22,"baiy","123456",remote_file,local_file)
    elif choice == "q":
        print("感谢使用，再见")
        exit()
    else:
        print("输入错误，请重新输入：")