import socket
import hashlib
d = {}
sock = socket.socket()
sock.bind(('127.0.0.2', 9090))
sock.listen()
conn, addr = sock.accept()

print ('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    hash = hashlib.md5()
    hash.update(data)
    value = (data.decode())
    key = hash.digest()
    d[value] = key
    print(value, d[value])
    conn.send(d[value])
    print("recved")
conn.close()