from socket import *
import time

class portScan():
    def __init__(self, host):
        print('Starting scan on host: ', host['ip'])
        print('MAC: ', host['mac'])
        self.t_IP = gethostbyname(host['ip'])
        self.start()

    def start(self):
        startTime = time.time()
        for i in range(0, 65535):
            s = socket(AF_INET, SOCK_STREAM)
            conn = s.connect_ex((self.t_IP, i))
            if (conn == 0):
                print('Port %d: OPEN' % (i,))
            s.close()
        print('Time taken:', time.time() - startTime)


