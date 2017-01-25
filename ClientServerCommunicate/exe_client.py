import socket
import sys

server_address = (sys.argv[1], 10075)
file_address = sys.argv[2]
print ( 'Connecting to %s port %s' % server_address )
print ( 'Transferring file: %s' %file_address )

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)

f = open (file_address, "rb")
l = f.read(1024)

while (l):
    sock.send(l)
    l = f.read(1024)

f.close()
sock.shutdown(socket.SHUT_WR)
sock.close()
print ( 'File transfer complete !' )