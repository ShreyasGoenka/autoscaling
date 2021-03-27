import socket
import time
import libvirt
import sys

conn = libvirt.open('qemu:///system')

if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)


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

    num_vms = 1
    running_mean_usage = 0


    track_cpu_usage1 = []
    track_cpu_usage2 = []
    track_num_vms = []
    track_total_load = []
    track_time = []

    scaleup_point = None


    num_iters = 100000 #2500 for high.
    for i in range(30):
        if num_vms == 1:
            loadServer(s, 135000, "12345 ")
            cpu_time1 = conn.lookupByName('ubuntu_server_1').getCPUStats(True)[0]['cpu_time']
            time.sleep(1)
            cpu_time2 = conn.lookupByName('ubuntu_server_1').getCPUStats(True)[0]['cpu_time']
            usage = 100 * (cpu_time2-cpu_time1) / 1000000000
            running_mean_usage = running_mean_usage*0.7 + 0.3*usage
            
            print(usage, running_mean_usage)

            track_cpu_usage1.append(usage)
            track_cpu_usage1.append(0)
            if len(track_time) == 0:
                track_time.append(0)
            else:
                track_time.append(track_time[-1] + 1)
            track_num_vms.append(num_vms)
            track_total_load.append(num_iters)

            if (running_mean_usage > 80):
                scaleup_point = track_time[-1]


if __name__ == "__main__":
    main()

# 52:54:00:56:e1:a9