import socket
import sys
from msg_recv_timeout import msg_recv_timeout

# Connect the socket to the port on the server given by the caller
server_address = (sys.argv[1], sys.argv[2])
print ( 'connecting to %s port %s' % server_address )

while True:
    try:
        message = 'bye'
        message = input('Type a message: ')
        
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
        
        if message == 'bye':
            raise Exception ('Conversation is over !')
        
        print ( 'sending "%s"' % message )
        sock.sendall(message.encode())
        
        returnmsg = str(msg_recv_timeout(sock))
        print ( 'received "%s"' % returnmsg)
    
    except Exception as v:
        print(v)
        break
    
    finally:
        sock.close()