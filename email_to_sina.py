import socket
import time
import smtplib
import urllib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def sendEmail(smtpserver,username,password,sender,receiver,subject,msghtml):
        msgRoot =MIMEMultipart('related')
        msgRoot['To']=','.join(receiver)
	msgRoot["From"] = sender
        msgRoot['Subject']= subject
        msgText = MIMEText(msghtml,'html','utf-8')
        msgRoot.attach(msgText)
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username,password)
	smtp.sendmail(sender,receiver,msgRoot.as_string())
        print "YES"
        smtp.quit()

def check_network():
        while True:
            try:
                result=urllib.urlopen('http://baidu.com').read()
                print result
                print "Network is Ready!"
                break
            except Exception ,e:
                print e
                print "Network is not ready,Sleep 5s..."
                time.sleep(5)
        return True

def get_ip_address():
        s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(("1.1.1.1",80))
        ipaddr=s.getsockname()[0]
        s.close()
        return ipaddr

if  __name__ == '__main__' :
        check_network()
        ipaddr= get_ip_address()
        sendEmail("smtp.sina.com",'your email account','password','sender',['receiver'],'IP Address of Raspberry PI',ipaddr)