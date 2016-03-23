#coding:utf-8
import socket,threading

'''def recvFromServer(sock):
    while 1:
        data = sock.recv(1024)
        print "Recv frome Server:"+data+"\n"
        if sock:
            pass
        else:
            break'''

def sendToServer(sock):
    while 1:
        sendto = raw_input()
        sock.send(sendto)
        if sendto=="exit":
            s.close()
            print "Closed connection with server!\n"
            break



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 2016))
# 接收欢迎消息:
print s.recv(1024)

#t1 = threading.Thread(target=recvFromServer, args=(s,))
t2 = threading.Thread(target=sendToServer, args=(s,))
#t1.start()
t2.start()
