import socket
import sys
import subprocess
import s_file
import s_msg

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 10000)
print ( 'Starting up on %s port %s' % server_address )
sock.bind(server_address)
sock.listen(10)

while True:

    print ( 'Waiting for a connection' )
    connection, client_address = sock.accept()
    print ( 'Client connected:', client_address )
    
    prjname = s_msg.recv (connection)
    
    filename = prjname + ".config"
    s_file.recv ( connection, filename )
    
    filename = prjname + ".json"
    s_file.recv ( connection, filename )
        
    filename = prjname + ".log"
    command = "./test.sh &> " + filename
    subprocess.call(command, shell=True)
    print ( 'Engine calculation completed !' )
    s_file.recv ( connection, filename )
        
    connection.close()

sock.close()



