from scan import Scan


class main():
    def __init__(self):
        print("Welcome")
        self.results = Scan(input('Enter IP range ex.192.168.1.1/24: '))
        self.getaway = input("Choose a getaway: ")
        self.target = input("Choose a target: ")
        self.prientAttaks()

    def prientAttaks(self):
        print("""[1] Disconnect Network
[2] Scan Port
[3] ARP Spoofing""")
        attack = input("=>")



if __name__ == '__main__':
    main()