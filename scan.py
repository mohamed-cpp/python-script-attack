import scapy.all as scapy
from mac_vendor_lookup import MacLookup

class Scan():
    def __init__(self, range):
        print('Scanning network:' + range)
        self.results = self.scanNetwork(range)
        self.scan_result(self.results)

    def mac_lookup(self, mac):
        try:
            return MacLookup().lookup(mac)
        except:
            return "Unknown"

    def scanNetwork(self, ip):
        arp_req = scapy.ARP(pdst=ip)
        # arp_req.pdst = ip // or
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_req_broadcast = broadcast / arp_req
        # answered, unanswered = scapy.srp(arp_req_broadcast, timeout=1)
        answered = scapy.srp(arp_req_broadcast, timeout=5, retry=3, verbose=False)[0]
        # arp_req_broadcast.show()
        # print(broadcast.summary()) // summary
        # scapy.ls(scapy.ARP()) // see all fun~
        # scapy.arping(ip) // scapy arping alone

        MACs_list = []

        for el in answered:
            device = {"ip": el[1].psrc, "mac": el[1].hwsrc, "vendor": self.mac_lookup(el[1].hwsrc)}
            MACs_list.append(device)
        return MACs_list

    def scan_result(self, results):
        print("No.\t\tIP\t\tMac Address\t\tMac Vendor\n-----------------------------------------------------------------------")
        number = 1
        for result in results:
            print("[" + str(number) + "]\t\t" + result["ip"] + "\t" + result["mac"] + "\t" + result["vendor"])
            number += 1