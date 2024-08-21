import socket

host = "localhost"
port = 8080

# create object of socket on client side
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server by providing same host and port that has been used on server side.
sock.connect((host, port))

# receive message from server
message = sock.recv(1024).decode()
print("Message: ", message)

sock.close()