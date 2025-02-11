import scapy.all as scapy
from scapy.layers import http
from termcolor import colored
import signal
import sys

def def_handler(sig, frame):
    print(colored("[+] Exiting Sniffer...", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def process_packet(packet):
    cred_keywords = ["login", "password", "user", "username", "pass", "mail"]

    if packet.haslayer(http.HTTPRequest):
        url = "http://" + packet[http.HTTPRequest].Host.decode() + packet[http.HTTPRequest].Path.decode()
        print(colored(f"\n[+] URL: {url}", "blue"))

        if packet.haslayer(scapy.Raw):
            try:
                response = packet[scapy.Raw].load.decode()
                for keyword in cred_keywords:
                    if keyword in response:
                        print(colored(f"\n[+] Possible credentials: {response}", "green"))
                        break
            except:
                pass

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def main():
    interface = ''
    sniff(interface)

if __name__ == '__main__':
    main()