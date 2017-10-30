#!/bin/bash

while true
do
{
	date1=`date +%Y%m%d_%H%M%S`
	h264str=$date1'.h264'
	mp4str=$date1'.mp4'
	raspivid -w 640 -h 480 -fps 25 -o $h264str -t 10000
	MP4Box -add $h264str $mp4str
	re=`./test1.sh`
	echo $re
	rm h264str
	sleep 1	
}
done


