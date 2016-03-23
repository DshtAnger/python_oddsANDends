#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-02-14 19:23:39
# @Author  : DshtAnger

'''
收取邮件分两步：
第一步：用poplib把邮件的原始文本下载到本地
第二部：用email解析原始文本，还原为邮件对象
'''

import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


# 输入邮件地址, 口令和POP3服务器地址:
email = "568274449@qq.com"#raw_input('Email: ')
password = "nhrfuvmexfepbdig"#raw_input('Password: ')
pop3_server = "pop.qq.com"#raw_input('POP3 server: ')

# 连接到POP3服务器:
server = poplib.POP3_SSL(pop3_server,995)
# 可以打开或关闭调试信息:
# server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print(server.getwelcome())
# 身份认证:
server.user(email)
server.pass_(password)
# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似['1 82923', '2 2184', ...]
print(mails)
# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index)
# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = '\r\n'.join(lines)

# 稍后解析出邮件:
msg = Parser().parsestr(msg_content)
#但是这个Message对象本身可能是一个MIMEMultipart对象，即包含嵌套的其他MIMEBase对象，嵌套可能还不止一层。
pass
pass
pass

# 可以根据邮件索引号直接从服务器删除邮件:
#server.dele(index)

# 关闭连接:
server.quit()