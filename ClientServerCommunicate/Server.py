import socket
import sys
import time


def recv_timeout(the_socket,timeout=0.1):
    #make socket non blocking
    the_socket.setblocking(0)
     
    #total data partwise in an array
    total_data=[]
    data=''
    
    #beginning time
    begin=time.time()
    while 1:
        #if you got some data, then break after timeout
        if total_data and time.time()-begin > timeout:
            break
         
        #if you got no data at all, wait a little longer, twice the timeout
        elif time.time()-begin > timeout*2:
            break
         
        #recv something
        try:
            data = the_socket.recv(8192)
            if data:
                total_data.append(data)
                #change the beginning time for measurement
                begin=time.time()
            else:
                #sleep for sometime to indicate a gap
                time.sleep(0.1*timeout)
        except:
            pass
        
    #join all parts to make final string
    return b''.join(total_data).decode()
    

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
    print ( 'client connected:', client_address )
        
    try:
        data = str(recv_timeout(connection))

        
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
