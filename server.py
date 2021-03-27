import socket
from _thread import *
import threading  
from threading import Thread

def computeSequenceSum(x):
    ans = 0
    for i in range(0, int(x)+1):
        ans += i
    print(ans)
    return ans


def ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port

    def run(self):
        data = conn.recv(x)
        # TODO: will maybe need to convert this byte string
        print("Data: ", data)
        computeSequenceSum(x)
        conn.send("done compute")



def multiThreadedServer():
    host_ip = ""
    port = 5555

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    s.bind((host_ip, port))

    threads = []

    while True:
        s.listen(5)
        conn, (ip, port) = s.accept()
        computeThread = ClientThread(ip, port)
        computeThread.start()
        threads.append(computeThread)

    for t in threads:
        t.join()


def singleThreadedServer():
    s = socket.socket()         
    port = 5555

    s.bind(('', port))
    s.listen()

    c, addr = s.accept()

    while True:
        data = c.recv(1024).decode()
        data = str(data)
        thread = Thread(target=computeSequenceSum, args=(data, ))


if __name__ == "__main__":
    singleThreadedServer()


