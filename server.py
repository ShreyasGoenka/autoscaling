import socket             

s = socket.socket()         
port = 5555

s.bind(('', port))
print("server socket bound")

while True:

    c, addr = s.accept()
    print("Got connection from". addr)
    c.close()





