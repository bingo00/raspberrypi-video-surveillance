import sys
import oss
from oss.oss_api import *
filename = sys.argv[1]
oss = OssAPI("OSS_access point name","access_key","access_secret")
res = oss.put_object_from_file("vss2017",filename,filename) #can just input when you run the python script
print "%s\n%s" % (res.status,res.read()) #print out the upload message, 200 is the success upload
