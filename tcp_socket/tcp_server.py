#coding:utf-8
import socket,threading

'''def sendToClient(sock, addr):    
    sock.send('Welcome to connect me !\n')
    while True:        
        sendto = raw_input()
        if sendto!="close":
            sock.send(sendto)
        else:
            sock.close()
            print 'Connection from %s:%s closed...\n' % addr
            break'''

def recvFromClient(sock,addr):
    sock.send('Welcome to connect me !\n')
    while 1:
        if not sock:
            break
        recvData = sock.recv(1024)
        if recvData =="exit":            
            break
        print "Recv from %s:%s :"%addr,recvData+"\n"
    sock.close()
    print 'Connection from %s:%s closed...\n' % addr     
            
            
   

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 2016))
s.listen(5)
print '[*]Waiting for connection...\n'

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    print '[+]Accept new connection from %s:%s...\n' % addr
    #t1 = threading.Thread(target=sendToClient, args=(sock, addr))
    t2 = threading.Thread(target=recvFromClient, args=(sock, addr))
    #t1.start()
    t2.start()