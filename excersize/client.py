import socket

s = socket.socket()
host = socket.gethostname()
port = 1380
s.connect((host, port))
while True:
    inp = input()
    if inp == "exit":
        s.close()
        break
    s.send(inp.encode())
    print(s.recv(1024).decode())
