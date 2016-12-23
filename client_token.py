# Echo client program
import socket
import string
import json
#import dict

HOST = 'daring.cwi.nl'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
#    print('Enter Name, Vendor, Red_ID and Price')
    s.sendall(b'iPhone,Apple,A1502,699')
    s.sendall(b'Galaxy_Ace,Samsung,B1457,499')
#    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))
