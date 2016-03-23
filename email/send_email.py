#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-02-14 19:23:39
# @Author  : DshtAnger

import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
#添加附件时使用
from email.MIMEMultipart import MIMEMultipart 
from email.MIMEBase import MIMEBase
'''
概述：
点“发送”，电子邮件就发出去了。这些电子邮件软件被称为MUA：Mail User Agent——邮件用户代理
Email从MUA发出去，不是直接到达对方电脑，而是发到MTA：Mail Transfer Agent——邮件传输代理,就是那些Email服务提供商，比如网易、新浪等等
Email到达新浪的MTA后,新浪的MTA会把Email投递到邮件的最终目的地MDA：Mail Delivery Agent——邮件投递代理。
Email到达MDA后，就静静地躺在新浪的某个服务器上，存放在某个文件或特殊的数据库里，我们将这个长期保存邮件的地方称之为电子邮箱。
收件人想要取到邮件，必须通过MUA从MDA上把邮件取到自己的电脑上

一封电子邮件的旅程就是：
    发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

编写程序来发送和接收邮件，本质上就是：
    1.编写MUA把邮件发到MTA
    2.编写MUA从MDA上收邮件

收邮件时，MUA和MDA使用的协议有两种：
    1.POP：Post Office Protocol，目前版本是3，俗称POP3
    2.IMAP：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱，等等

邮件客户端软件在发邮件时，会让你先配置SMTP服务器，也就是你要发到哪个MTA上。假设你正在使用163的邮箱，你就不能直接发到新浪的MTA上，因为它只服务新浪的用户，所以，你得填163提供的SMTP服务器地址：smtp.163.com，为了证明你是163的用户，SMTP服务器还要求你填写邮箱地址和邮箱口令，这样，MUA才能正常地把Email通过SMTP协议发送到MTA。

类似的，从MDA收邮件时，MDA服务器也要求验证你的邮箱口令，确保不会有人冒充你收取你的邮件，所以，Outlook之类的邮件客户端会要求你填写POP3或IMAP服务器地址、邮箱地址和口令，这样，MUA才能顺利地通过POP或IMAP协议从MDA取到邮件


163服务器地址如下:
POP3服务器:pop.163.com
SMTP服务器:smtp.163.com
IMAP服务器:imap.163.com
'''
def _format_addr(s):
    name, addr = parseaddr(s)#返回name为<>前部内容,addr为<>中邮箱地址内容
    return formataddr(  (   Header(name, 'utf-8').encode(),
                            addr.encode('utf-8') if isinstance(addr, unicode) else addr
                        )
                    )
# 输入Email地址和口令:
from_addr = "xjaks-dwxbb@163.com"#raw_input('Address: ')
password = "103MahpalXBB1010"#raw_input('Password: ')
# 输入收件人地址:
to_addr = "568274449@qq.com"#raw_input('To: ')
# 输入SMTP服务器地址:
smtp_server = "smtp.163.com"#raw_input('SMTP server: ')

#创建邮件对象
'''
#1.纯文本邮件正文
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

#2.html邮件正文
msg = MIMEText('<html><body><h1>Hello</h1>' +'<p>send by <a href="http://www.python.org">Python</a>...</p>' +'</body></html>', 'html', 'utf-8')

#3.需要使用附件时创建的邮件对象，不使用附件时无需创建
msg = MIMEMultipart() 

#4.在邮件正文中插入图片的html邮件，按照发送带附件邮件的方式，在html里进行引用即可，邮件效果不出现附件
msg = MIMEText('<html><body><h1>Hello</h1>' +'<p>send by <a href="http://www.python.org">Python</a>...</p>' + '<p><img src="cid:0"></p>' + '</body></html>', 'html', 'utf-8')

#5.若发送同时支持HTML和Plain格式邮件
msg = MIMEMultipart('alternative')
msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))

'''

msg = MIMEMultipart('alternative')
msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))

#邮件头部信息
msg['From'] = _format_addr(u'我是发送者<%s>' % from_addr)
msg['To'] = _format_addr(u'我是接收者<%s>' % to_addr)
msg['Subject'] = Header(u'使用python发送邮件', 'utf-8').encode()


'''
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('/home/DshtAnger/Pictures/send.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型:
    mime = MIMEBase('image', 'jpg', filename='send.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='send.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
'''

# SMTP协议默认端口是25
server = smtplib.SMTP(smtp_server, 25)

#s可以打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)

#登录SMTP服务器
server.login(from_addr, password)

#发邮件，可以一次发给多个人、传入一个list，as_string()把邮件正文的MIMEText对象变成str。
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
