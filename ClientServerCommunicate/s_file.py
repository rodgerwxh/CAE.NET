import socket

def send (server_address, filename):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    f = open (filename, "rb")
    l = f.read(1024)
    while (l):
        sock.send(l)
        l = f.read(1024)
    f.close()
    sock.shutdown(socket.SHUT_WR)
    print('File {} sent.'.format(filename) )
    sock.close()
    
def recv (sock, filename):
    f = open(filename,'wb') #open in binary
    l = sock.recv(1024)
    while (l):
        f.write(l)
        l = sock.recv(1024)
    f.close()
    print ( 'File %s received.' % filename )
    sock.close()