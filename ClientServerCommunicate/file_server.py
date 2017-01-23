import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, sys.argv[2])
print ( 'Starting up on %s port %s' % server_address )
sock.bind(server_address)
sock.listen(1)

while True:

    print ( 'Waiting for a connection' )
    connection, client_address = sock.accept()
    print ( 'Client connected:', client_address )
	
    i=1
    f = open('file_'+ str(i)+".json",'wb') #open in binary
    i=i+1
    while (True):       
    # recibimos y escribimos en el fichero
        l = sc.recv(1024)
        while (l):
                f.write(l)
                l = sc.recv(1024)
    f.close()


    connection.close()

sock.close()