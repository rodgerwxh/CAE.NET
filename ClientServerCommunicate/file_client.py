import socket
import sys
import scom 

server_address = (sys.argv[1], 10075)
file_address = sys.argv[2]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
    
print ( 'Connecting to %s port %s' % server_address )
print ( 'Transferring file: %s' %file_address )

scom.send_msg (sock, file_address)
scom.send_file ( sock, file_address )

filename = "test1.txt"
scom.recv_file ( sock, filename )

scom.send_msg (sock, filename)
scom.send_file ( sock, filename )

filename = "test2.txt"
scom.recv_file ( sock, filename )

scom.send_msg (sock, filename)
scom.send_file ( sock, filename )

filename = "test3.txt"
scom.recv_file ( sock, filename )

scom.send_msg (sock, filename)
scom.send_file ( sock, filename )



sock.close()


print ( 'File transfer complete !' )