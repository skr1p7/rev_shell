import socket
def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("192.168.42.253",8080))
	s.listen(1)
	print "*"*10 + "waiting" + "*"*10
	connection, address = s.accept()
	print "Connection successful to the IP> ", address
	while True:
		command = raw_input("$ ")
		if "q" in command:
			connection.send("connection closed")
			connection.close()
			break
		else:
			connection.send(command)
			print connection.recv(1024)

connect()