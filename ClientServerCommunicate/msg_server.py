import socket
import sys
from msg_recv_timeout import msg_recv_timeout


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, sys.argv[2])
print ( 'starting up on %s port %s' % server_address )
sock.bind(server_address)
sock.listen(1)

while True:

    print ( 'waiting for a connection' )
    connection, client_address = sock.accept()
    print ( 'client connected:', client_address )
        
    try:
        data = str(msg_recv_timeout(connection))

        
        print ( 'received "%s"' % data )
        if data == 'bye':
            raise Exception ( 'Conversation is over !' )
        
        data = data.upper()
        connection.sendall(data.encode())
            
    except Exception as ve:
        print (ve)

    finally:
        connection.close()
    
    connection.close()
