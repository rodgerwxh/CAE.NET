import socket
import sys
import scom

server_address = (sys.argv[1], 10075)
print ( 'Connecting to %s port %s' % server_address )
prjname = sys.argv[2]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
    
scom.send_msg ( sock, prjname )
    
filename = prjname + ".config"
f = open (filename, "wb")
f.write(prjname.encode())
f.close()
scom.send_file (sock, filename)
   
filename = prjname + ".json"
scom.send_file (sock, filename)
    
filename = prjname + ".log"
scom.recv_file (sock, filename)

print ( 'Simulation completed successfully !' )

sock.close()
		