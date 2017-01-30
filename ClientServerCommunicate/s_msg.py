import socket
import time

def send ( sock, msg ):
    sock.sendall(msg.encode())

def recv ( sock, timeout=0.1 ):
        
    #make socket non blocking
    sock.setblocking(0)
     
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
            data = sock.recv(8192)
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
    return str(b''.join(total_data).decode())