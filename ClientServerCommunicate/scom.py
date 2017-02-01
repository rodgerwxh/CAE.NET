import socket

def send_null (sock):
    sock.send(' '.encode())

def recv_null(sock):
    sock.recv(1024)
    
def send_int32 ( sock, num ):
    l = '%32d' % num
    sock.sendall(l.encode())

def recv_int32 ( sock ):
    num = int(sock.recv(32))
    return num

def send_msg ( sock, msg ):
    send_int32 (sock,len(msg))
    sock.sendall(msg.encode())

def recv_msg ( sock ):
    l = recv_int32(sock)
    msg = sock.recv(l).decode()
    return msg
    
def send_file (sock, filename):
    f = open (filename, "rb")
    data = f.read()
    send_int32 (sock,len(data))
    sock.sendall(data)
    f.close()
    recv_null(sock)
    print('File %s sent.' % filename )
    
def recv_file (sock, filename):
    f = open(filename,'wb') #open in binary
    l = recv_int32(sock)
    lc = 0
    while l > lc:
        data = sock.recv(1024)
        if not data:
            break
        lc += len(data)
        f.write(data)
    f.close()
    send_null(sock)
    print ( 'File %s received.' % filename )