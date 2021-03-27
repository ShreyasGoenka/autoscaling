import socket
import time

def testClient():
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    except socket.error as err: 
        print ("socket creation failed with error %s" %(err))


    server_ip = '192.168.123.165'
    port = 5555

    s.connect((server_ip, port))

def loadServer(s, num_iters, val):
    for i in range(num_iters):
        s.send(str(val).encode())


def main():
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    except socket.error as err: 
        print ("socket creation failed with error %s" %(err))


    server_ip = '192.168.123.165'
    port = 5555

    s.connect((server_ip, port))

    for i in range(60):
        loadServer(s, 1000, "12345 ")
        time.sleep(1)

if __name__ == "__main__":
    main()


