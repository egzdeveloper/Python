import scapy.all as scapy
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Arp Scanner')
    parser.add_argument('-t', '--target', required=True, dest='target', help='Host / IP to scan')
    args = parser.parse_args()
    return args.target

def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet = broadcast_packet/arp_packet
    answered, unanswered = scapy.srp(arp_packet, timeout=1, verbose=False)

    clients_list = []
    for element in answered:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)

    return clients_list

def print_results(results):
    if not results:
        print("No devices found.")
    else:
        print("IP Address\t\tMAC Address")
        print("-----------------------------------------")
        for client in results:
            print(f"{client['ip']}\t\t{client['mac']}")

def main():
    target = get_args()
    scan_result = scan(target)
    print_results(scan_result)

if __name__ == "__main__":
    main()