#TODO Wrap in appropriate try catch methods
import json
from socket import socket, gethostbyname,gethostname,AF_INET,SOCK_STREAM    

class Proxy(object):
    
    def setup(self):

        self.sock = socket(AF_INET, SOCK_STREAM)
        self.name = gethostname()
        self.host_ip = gethostbyname(self.name)
        self.server_address = (self.host_ip,1351)
    
    def push(self,updatedState):
        
        self.setup()
        self.sock.connect(self.server_address)
        data = {"operation":"push","state":updatedState}
        data = json.dumps(data)
        self.sock.send(data.encode())
        self.sock.close()
    
    def pull(self):

        self.setup()
        self.sock.connect(self.server_address)
        request = {"operation":"pull"}
        request = json.dumps(request)
        self.sock.send(request.encode())

        response = self.sock.recv(128).decode()
        self.sock.close()
        
        return json.loads(response)
    
def test():

    p = Proxy()
    j ={"Heating":True, "Lights": False}
    print(p.pull())
    p.push(j)

if __name__ == "__main__":
    test()