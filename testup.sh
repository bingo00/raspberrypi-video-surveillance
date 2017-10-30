#!/bin/bash

date1=`date +%Y%m%d_%H%M%S`
h264str=$date1'.h264'
mp4str=$date1'.mp4'
raspivid -w 640 -h 480 -fps 5 -o $h264str
MP4Box -add $h264str $mp4str
re=`./test1.sh`
echo $re
sleep 5	