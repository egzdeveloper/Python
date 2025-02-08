import argparse
import re
import subprocess
from termcolor import colored

def get_arguments():
    parser = argparse.ArgumentParser(description='MAC changer')
    parser.add_argument('-i', '--interface', required=True, dest='interface', help='Network interface name')
    parser.add_argument('-m', '--mac', required=True, dest='mac_address', help='New MAC address')
    return parser.parse_args()

def is_valid_input(interface, mac_address):
    is_valid_interface = re.match(r'^[e][n|t][s|h]\d{1,2}$]', interface)
    is_valid_mac_address = re.match(r'^[A-Fa-f0-9{2][:]{5}[A-Fa-f0-9]{2}$', mac_address)
    return is_valid_interface and is_valid_mac_address

def change_mac_address(interface, mac_address):
    if is_valid_input(interface, mac_address):
        subprocess.run(['ifconfig', interface, 'down'])
        subprocess.run(['ifconfig', interface, 'hw', 'ether', mac_address])
        subprocess.run(['ifconfig', interface, 'up'])
        print(colored(f"\n[+] MAC address changed to {mac_address}", 'green'))
    else:
        print(colored(f'\n[!] Input data is invalid', "red"))

def main():
    args = get_arguments()
    change_mac_address(args.interface, args.mac_address)

if __name__ == '__main__':
    main()