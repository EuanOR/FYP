from socket import socket, AF_INET, SOCK_STREAM, gethostname,gethostbyname

import time
import json

curState = {dict}

sock = socket(AF_INET, SOCK_STREAM)
name = gethostname()
host_ip = gethostbyname(name)

server_address = (host_ip, 1351)

print('*** Server is starting up on %s port %s ***' % server_address)
# Bind the socket to the host and port
sock.bind(server_address)

# Listen for one incoming connections to the server
sock.listen(1)


while True:

    print('*** Waiting for a connection ***')
    # accept() returns an open connection between the server and client, along with the address of the client
    connection, client_address = sock.accept()
    
    try:
        print('connection from', client_address)
            
        data = connection.recv(128).decode()
        print(data)
        data = json.loads(data)
    
        if data["operation"] == "push":
            curState = data["state"]
            print(curState)
        
        elif data["operation"] == "pull":
            sendState = json.dumps(curState)
            connection.send(sendState.encode())
            
    
    finally:
        connection.close()

sock.close()