import socket

def send (sock, filename):
    f = open (filename, "rb")
    data = f.read()
    l = len(data)
    l_str = '%32d' % l
    sock.sendall (l_str.encode())
    sock.sendall(data)
    f.close()
    sock.recv(128)
    print('File %s sent.' % filename )
    
def recv (sock, filename):
    f = open(filename,'wb') #open in binary
    l = int(sock.recv(32))
    lc = 0
    while l > lc:
        data = sock.recv(1024)
        if not data:
            break
        lc += len(data)
        f.write(data)
    f.close()
    sock.send('ok'.encode())
    print ( 'File %s received.' % filename )
