import socket

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
except socket.error as err: 
    print ("socket creation failed with error %s" %(err))


server_ip = '192.168.123.165'
port = 5555

s.connect((server_ip, port))