import socket
import sys
import s_file
import s_msg

server_address = (sys.argv[1], 10075)
print ( 'Connecting to %s port %s' % server_address )
prjname = sys.argv[2]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
    
s_msg.send ( sock, prjname )
    
filename = prjname + ".config"
f = open (filename, "wb")
f.write(prjname.encode())
f.close()
s_file.send (sock, filename)
   
filename = prjname + ".json"
s_file.send (sock, filename)
    
filename = prjname + ".log"
s_file.send (sock, filename)

print ( 'Simulation completed successfully !' )

sock.close()
		