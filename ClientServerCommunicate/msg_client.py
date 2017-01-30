import socket
import sys
import s_msg as s

# Connect the socket to the port on the server given by the caller
server_address = (sys.argv[1], 10075)
print ( 'connecting to %s port %s' % server_address )

while True:
    try:
        message = 'bye'
        message = input('Type a message: ')
        
        if message == 'bye':
            raise Exception ('Conversation is over !')
            
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
        
        print ( 'sending "%s"' % message )
        s.send(sock, message)
        
        returnmsg = s.recv(sock)
        print ( 'received "%s"' % returnmsg)
    
    except Exception as v:
        print(v)
        break
    
    finally:
        sock.close()