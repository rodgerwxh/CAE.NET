import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 10000)
print ( 'Starting up on %s port %s' % server_address )
sock.bind(server_address)
sock.listen(10)

i = 1
while True:

    print ( 'Waiting for a connection' )
    connection, client_address = sock.accept()
    print ( 'Client connected:', client_address )

    f = open('file_'+ str(i)+".json",'wb') #open in binary
    i=i+1

    l = connection.recv(1024)
    while (l):
         f.write(l)
         l = connection.recv(1024)
    f.close()
    connection.close()
    print ( 'File transfer complete !' )

sock.close()