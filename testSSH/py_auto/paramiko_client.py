#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   paramiko_client.py
@Time    :   2019/09/02
@Author  :   Yang.Lu
@Version :   1.0
@Desc    :   paramiko class
'''

import time
import paramiko
import configparser 
import os

class ParamikoClient:
    def __init__(self, cfg_file, section, log_dir):
        self.config = configparser.ConfigParser()
        self.config.read(cfg_file)
        self.ssh_client = paramiko.SSHClient()
        #self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.set_missing_host_key_policy(paramiko.WarningPolicy())
        self.sftp_client = None
        self.client_state = 0
        self.section = section
        self.log_dir = log_dir

    def connect(self):
        try:
            self.ssh_client.connect(hostname=self.config.get(self.section, 'host'),
                                port=self.config.getint(self.section, 'port'),
                                username=self.config.get(self.section, 'username'),
                                password=self.config.get(self.section, 'password'),
                                timeout=self.config.getfloat(self.section, 'timeout'))
            self.client_state = 1
        except Exception as e:
            print(e,':Unable to connect to port',self.config.getint(self.section, 'port'),
                  'on',self.config.get(self.section, 'host'))
            try:
                self.ssh_client.close()
            except:
                pass

    def close(self):
        self.ssh_client.close()

    def run_cmd(self, cmd_str):
        _, stdout, stderr = self.ssh_client.exec_command(cmd_str)
        # print('stdout:\n', self.config.get(self.section, 'host'), stdout.read().decode("utf-8"))
        # print('stderr:\n', self.config.get(self.section, 'host'), stderr.read().decode("utf-8"))
        if (self.log_dir):
            f = open("./"+self.log_dir+"/"+self.section, 'a+')
            #print("./"+self.log_dir+"/"+self.section)
            #log_time = time.strftime("[TEST TIME][%Y%m%d %H:%M:%S]\n", time.localtime())
            #f.write(log_time)
            f.write(stdout.read().decode("utf-8"))
            f.write(stderr.read().decode("utf-8"))
            f.close()

    def sftp_upload(self, localpath, remotepath):
        if self.client_state == 0:
            self.connect()
        if not self.sftp_client:
            try:
                self.sftp_client = paramiko.SFTPClient.from_transport(self.ssh_client.get_transport())
            except Exception as e:
                print(e)
        self.sftp_client.put(localpath, remotepath)

    def sftp_download(self, remotepath, localpath):
        if self.client_state == 0:
            self.connect()
        if not self.sftp_client:
            try:
                self.sftp_client = paramiko.SFTPClient.from_transport(self.ssh_client.get_transport())
            except Exception as e:
                print(e)
        self.sftp_client.get(remotepath, localpath)
        

    def sftp_download_dir(self, remotepath, localpath):
        if self.client_state == 0:
            self.connect()
        if not self.sftp_client:
            try:
                self.sftp_client = paramiko.SFTPClient.from_transport(self.ssh_client.get_transport())
            except Exception as e:
                print(e)
        
        files = self.sftp_client.listdir(remotepath)
        #print(files)
        for f in files:
            self.sftp_client.get(os.path.join(remotepath, f), os.path.join(localpath, f))
