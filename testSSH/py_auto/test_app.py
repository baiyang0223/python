#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   paramiko_client.py
@Time    :   2019/09/02
@Author  :   Yang.Lu
@Version :   1.0
@Desc    :   paramiko class
'''

import os
import sys
import time
from multiprocessing import Pool
from paramiko_client import ParamikoClient


def test_proc(section,log_dir):
    time.sleep(3)
    print("test_proc end")
    pass

def test_process_sync(func, section,log_dir):
    print("sync start")
    pool = Pool()
    pool.apply(func, args=(section, log_dir, ))
    pool.close()
    print("sync End")

def test_process_async(func, section,log_dir):
    print("async start")
    pool = Pool()
    pool.apply_async(func, args=(section, log_dir, ))
    pool.close()
    #pool.join()
    print("async End")

def dms_ap_start(section,log_dir):
    time.sleep(3)
    client = ParamikoClient('config.ini', section, log_dir)
    client.connect()
    client.run_cmd('killall send_image_mipi_rx_tx_compare')
    client.run_cmd('killall send_image_mipi')
    client.run_cmd('cp /mnt/chip_check/testmipi/zu3-mipi-bypass/libimage_send_mipi.so /lib/')
    client.run_cmd('cp /mnt/chip_check/dms_adas/libbif.so /lib/')
    client.run_cmd('cd /mnt/chip_check/dms_adas/;./send_image_mipi -s 1280x720 -l 1 -v 1 -c 30 -n 1 -k dms')
    client.close()
    pass

def dms_cp_start(section,log_dir):
    client = ParamikoClient('config.ini', section, log_dir)
    client.connect()
    test_process_async(dms_ap_start, "ap",log_dir)
    client.run_cmd('/app/dms/dms.sh')
    client.run_cmd('cat /userdata/dms.txt')
    #client.sftp_download("/userdata/dms.txt",log_dir)
    dms_log_path=os.path.join(log_dir, "log")
    os.mkdir(dms_log_path)
    client.sftp_download_dir("/userdata/log/",dms_log_path)
    client.close()
    pass

def dms_cp_exit(section,log_dir):
    pass

def dms_ap_exit(section,log_dir):
    client = ParamikoClient('config.ini', section, log_dir)
    client.connect()
    client.run_cmd('killall send_image_mipi_rx_tx_compare')
    client.run_cmd('killall send_image_mipi')
    client.close()
    pass

def adas_test(log_dir):
    print("Not Support");
    pass


def sk_ap_start(section,log_dir):
    time.sleep(3)
    client = ParamikoClient('config.ini', section, log_dir)
    client.connect()
    client.run_cmd('killall send_image_mipi_rx_tx_compare')
    client.run_cmd('killall send_image_mipi')
    client.run_cmd('cp /mnt/chip_check/testmipi/zu3-mipi-bypass/libimage_send_mipi.so /lib/')
    client.run_cmd('cp /mnt/chip_check/dms_adas/libbif.so /lib/')
    client.run_cmd('cd /mnt/chip_check/dms_adas/;./send_image_mipi -s 1920x1080 -l 1 -v 1 -c 30 -n 1 -k sk')
    client.close()
    pass

def sk_cp_start(section,log_dir):
    client = ParamikoClient('config.ini', section, log_dir)
    client.connect()
    client.run_cmd('echo performance > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor')
    client.run_cmd('echo performance > /sys/devices/system/cpu/cpu1/cpufreq/scaling_governor')
    client.run_cmd('echo 105000 >  /sys/devices/virtual/thermal/thermal_zone0/trip_point_0_temp')
    client.run_cmd('echo 105000 >  /sys/devices/virtual/thermal/thermal_zone0/trip_point_1_temp')
    client.run_cmd('echo 120000 >  /sys/devices/virtual/thermal/thermal_zone0/trip_point_2_temp')
    client.run_cmd('echo 0 > /sys/module/x2_mipi_host/parameters/mipi_host_notimeout')
    client.run_cmd('echo 1 > /sys/module/x2_mipi_host/parameters/mipi_host_nocheck')

    client.run_cmd('export BMEM_CACHEABLE=false')
    test_process_async(sk_ap_start, "ap",log_dir)
    client.run_cmd('cd /app/sk/ && /app/sk/adas-rt/hobot-adas-workflow ./adas-rt/config/global.json')
    #client.run_cmd('cat /tmp/log')
    client.close()
    pass

def sk_cp_exit(section,log_dir):
    pass

def sk_ap_exit(section,log_dir):
    client = ParamikoClient('config.ini', section, log_dir)
    client.connect()
    client.run_cmd('killall send_image_mipi_rx_tx_compare')
    client.run_cmd('killall send_image_mipi')
    client.close()
    pass

def sk_test(log_dir):
    sk_cp_start("cp",log_dir)
    sk_ap_exit ("cp",log_dir)
    sk_cp_exit ("cp",log_dir)
    pass

def dms_test(log_dir):
    dms_cp_start("cp",log_dir)
    dms_ap_exit ("cp",log_dir)
    dms_cp_exit ("cp",log_dir)
    pass


def dms_sftp_test(section,log_dir):
    client = ParamikoClient('config.ini', section, log_dir)
    client.connect()
    client.sftp_download_dir("/userdata/log/",log_dir)
    client.close()
    pass


if __name__=='__main__':
    log_dir = time.strftime("%Y%m%d_%H%M%S", time.localtime())+'_test'
    os.mkdir(log_dir)
    if (len(sys.argv) == 2 and sys.argv[1] == 'sk'):
        print('Start sk test')
        sk_test(log_dir)
        print('Emd sk test ' + log_dir)
    elif (len(sys.argv) == 2 and sys.argv[1] == 'dms'):
        print('Start dms test')
        dms_test(log_dir)
        print('End dms test: ' + log_dir)
    elif (len(sys.argv) == 2 and sys.argv[1] == 'adas'):
        print('Start adas test')
        adas_test(log_dir)
        print('End adas test')
    elif (len(sys.argv) == 2 and sys.argv[1] == 'auto'):
        print('Start sk test')
        sk_test(log_dir)
        print('Emd sk test ' + log_dir)
        print('Start dms test')
        dms_test(log_dir)
        print('End dms test: ' + log_dir)
    elif (len(sys.argv) == 2 and sys.argv[1] == 'test'):
        #test_process_sync(test_proc, "ap",log_dir)
        
        #test_process_async(test_proc, "ap",log_dir)
        #time.sleep(5)
        dms_sftp_test("cp",log_dir )
    else:
        os.rmdir(log_dir)
        print("Input " + sys.argv[0] + " sk/dms/adas")

    
