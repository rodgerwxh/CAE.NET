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
 
    
    


# Connect the socket to the port on the server given by the caller
server_address = (sys.argv[1], 10075)
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
        
        returnmsg = str(recv_timeout(sock))
        print ( 'received "%s"' % returnmsg)
    
    except Exception as v:
        print(v)
        break
    
    finally:
        sock.close()