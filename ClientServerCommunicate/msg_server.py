import socket
import sys
import s_msg


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 10000)
print ( 'starting up on %s port %s' % server_address )
sock.bind(server_address)
sock.listen(1)

while True:

    print ( 'waiting for a connection' )
    connection, client_address = sock.accept()
    print ( 'client connected: %s port %s' % client_address )
        
    try:
        data = s_msg.recv(connection)

        print ( 'Received "%s"' % data )
        if data == 'bye':
            raise Exception ( 'Conversation is over !' )
        
        data = data.upper()
        print ( 'Converted "%s"' % data )
        s_msg.send ( connection, data )
            
    except Exception as ve:
        print (ve)

    finally:
        connection.close()
    
sock.close()
