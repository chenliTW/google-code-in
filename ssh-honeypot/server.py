import socket 
 
host = 'localhost'
port = 8998
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR ,1)
s.bind((host,port))
s.listen(2)
 
while 1:
    c,a = s.accept()
    print("Connected from:".format(a))
    while 1:
        data = c.recv(1024)
        print(data)
        c.sendall(b"SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3\r\n")
        data = c.recv(1024)
        print(data)
        c.sendall(b"")
        data = c.recv(1024)
        print(data)
        if not data:
            break
        result=b"haah"
        if len(result.strip()) != 0:
            c.sendall(result)
        else:
            c.sendall("Done")
    c.close
s.close()