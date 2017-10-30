# raspberrypi-video-surveillance
using bash &amp; python script to upload video to alicloud

The project's aim is for using the raspberry pi to upload video surveillance files to the alicloud, the general steps is divided into three:
1. prepare the python environment for uploading
2. find out the newest video files in the dir
3. upload the file though python script (which is done auto with the help of bash script)

For prepare:
enable the camera module (not usb module) of raspberry pi with: sudo raspi-config
python -m pip install oss

you can use the follow command to test if the module is on
raspistill -v -o test.jpg

if you want to change the *.h264 video files to *.mp4 files, you can first install gpac
sudo apt-get update
sudo apt-get install gpac

then you can change the files via:
MP4Box -add filename.h264 filename.mp4

for taking videos, we can use 
raspivid -w 640 -h 480 -fps 25 -o $outfilename -t 10000
to record a .h264 video, for more information you can see raspivid --h

here in the python script, the package "oss.oss_api" is needed, so just install it with your python pip or sth else...
for the upload part, you need to know what is your server key & secret in order to access it.
the python script only has the function of uploading, very sorry for that, and the continue uploading is done in the bash script

for the basic bash script, you need to chmod +x *.sh to let it be runable
chmod +x test1.sh
chmod +x upload.sh
chmod +x testup.sh (just for testing whether it can be uploaded)

so the last job is to run the upload.sh by
./upload.sh
and enjoy your uploading!

the video files here is saved according to the raspberry pi time, so remember to set it with your time zone correctly, or it might be something wrong. The raspivid parameters can be changed in the upload.sh, also the sleep time (it's prepared for breaking with ctrl + c ).


The testup.sh is just for testing...

Old version of uploading script is also here, with the AWS_S3.py, and the command line in raspberry pi is done within the python script, so running the script can infinite upload the video surveillance files

The email_to_sina.py is a python script to send a email with the IP address of raspberry pi in local network to the receiver, just for convenient connection by remote computer connection.

Hope everyone have fun with raspberrypi and video surveillance!

We are VSS2017, We see what you can't see ^_^

