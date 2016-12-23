# Echo server program
import socket
import string
import json

l=[]
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            tokens = data.split(',')
            
            d={ 'name': tokens[1],
                'vendor': tokens[2],
                'id': tokens[3],
                'price': tokens[4]
            }
#			print(d)
            l.append(d)
			
            if not data: break
            conn.sendall(data)
input("\n\nНажмите Enter чтобы выйти .")