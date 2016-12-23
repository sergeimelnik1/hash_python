import socket

sock = socket.socket()
sock.connect(('127.0.0.2', 9090))

while True:
    msg = input()
    sock.send(msg.encode())
    data = sock.recv(1024)
    print (data)

sock.close()