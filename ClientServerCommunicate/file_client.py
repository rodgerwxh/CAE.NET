import socket
import sys
import s_file as s

server_address = (sys.argv[1], 10075)
file_address = sys.argv[2]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
    
print ( 'Connecting to %s port %s' % server_address )
print ( 'Transferring file: %s' %file_address )

s.send ( sock, file_address )


print ( 'File transfer complete !' )