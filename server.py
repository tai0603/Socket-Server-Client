import socket

host = "localhost"
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating socket object
sock.bind((host, port)) # binds the socket with the given IP and port

# server is listening and accept maximum one connection at a time
sock.listen(1)
print("The server is running and listening on port: ", port)

while True:
	# server is accepting the connection from clients
	connection, address = sock.accept() # accept return two things -> connection and address of the client.
	print("Client", connection, "has joined us recently with address: ", address)

	# setting up message from send
	message = "Hello from Server to Client"
	connection.send(message.encode()) # send message in form of bytes

	instr = input("Enter exit to disconnect the server: ")
	if instr == "exit":
		comfirm = input("Disconnecting the server..\nProceed (Y/n)? ")
		if comfirm == "Y" or comfirm == "y":
			break
		elif comfirm == "N" or comfirm == "n":
			pass
	else:
		pass

sock.close()