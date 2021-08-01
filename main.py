from scan import Scan
from portScan import portScan

class main():
    def __init__(self):
        print("Welcome")
        self.results = Scan(input('Enter IP range ex.192.168.1.1/24: ')).results
        self.getaway = int(input("Choose a getaway: ")) -1
        self.target = int(input("Choose a target: ")) - 1
        self.prientAttaks()

    def prientAttaks(self):
        print("""[1] Disconnect Network
[2] Scan Port
[3] ARP Spoofing""")
        attack = input("=>")
        if attack == '2':
            portScan(self.results[self.target])



if __name__ == '__main__':
    main()