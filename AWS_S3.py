import sys
import os
import commands
# import boto
# import boto.s3.connection
from boto.s3.key import Key
from boto3.session import Session
import boto3
aws_key=''
aws_secret=''

session = Session(aws_access_key_id=aws_key,aws_secret_access_key=aws_secret,region_name='eu-central-1')

s3 = session.resource('s3')
client = session.client('s3')

#for bucket in s3.buckets.all():
#	print('bucket name:%s'%bucket.name)
os.system('mkdir `date +%y%m%d`')
output_date=os.popen('date +%y%m%d')
string_date=output_date.read()
string_date=string_date.replace("\n","")
os.system('mkdir `date +%y%m%d`')
#try it to unlimit loop
while 1:
    #os.system('mkdir `date +%y%m%d`')
    output1=os.popen('date -d "today" +"%Y%m%d_%H%M%S"')
    string=output1.read()
    string1='./'+string_date+'/'+string.replace("\n","")+'.jpg'
    string2='raspistill -h 640 -w 480 -t 200 -q 5 -o '+string1
    os.system(string2)
    bucket = 'binvss'
    output2=os.popen('date -d "today" +"%Y%m%d_%H%M"')
    string3=output2.read().replace("\n","")+'/'
    objkey = string3+string.replace("\n","")+'.jpg'

    s3.Object('binvss',string3).put()
    #upload file
    data = open(string1,'rb')
    file_obj = s3.Bucket(bucket).put_object(Key=objkey, Body=data)

    #print bucket obj
    #bucket = s3.Bucket('binvss')
    #for obj in bucket.objects.all():
    #	print(obj.key)
    print 'ending upload',string1
