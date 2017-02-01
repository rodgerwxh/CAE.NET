import socket
import sys
import scom

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
    print ( 'Client connected: %s port %s' % client_address )

    filename = scom.recv_msg (connection)
    scom.recv_file ( connection, filename )
    scom.send_file ( connection, filename )
    
    filename = scom.recv_msg (connection)
    scom.recv_file ( connection, filename )
    scom.send_file ( connection, filename )
    
    filename = scom.recv_msg (connection)
    scom.recv_file ( connection, filename )
    scom.send_file ( connection, filename )
    
    filename = scom.recv_msg (connection)
    scom.recv_file ( connection, filename )
    
    connection.close()

sock.close()