#!/bin/bash
########################################################################
# File Name: cw_test.sh
# Author: Yang. Lu
# mail: yang.lu@horizon.ai
# Created Time: 2019-09-24
# Func: Excute the auto-test python script
#########################################################################
echo "Usage: $0 dms/sk/adas/auto"
declare -i loop=0
while :
do
	echo "test $loop"
	python3 test_app.py $1
	loop=$(($loop+1))
	# ps -aux|grep "python3 get_power.py"| grep -v grep | awk '{print $2}' | xargs kill -9
	sleep 1
done
# rm `grep -nr  "PASX"  | cut -d "/" -f 1` -r
