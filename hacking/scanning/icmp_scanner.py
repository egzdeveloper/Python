import argparse
import signal
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored

def def_handler(sig, frame):
    print(colored(f"\[!] Exiting...\n", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_args():
    parser = argparse.ArgumentParser(description='Get active host in a network (ICMP)')
    parser.add_argument('-t' '--target', required=True, dest='target', help='Host or range to scan')
    args = parser.parse_args()
    return args.target

def parse_target(target_str):
    # 192.168.1.1-100
    target_str_split = target_str.split('.') # ["192", "168", "1", "1-100"]
    first_three_octets = '.'.join(target_str_split[:3])

    if len(target_str_split) == 4:
        if '-' in target_str_split[3]:
            start, end = target_str_split[3].split('-')
            return [f"{first_three_octets}.{i}" for i in range(int(start), int(end) + 1)]
        else:
            return [target_str]
    else:
        print(colored('Invalid IP or range format', "red"))

def host_discovery(target):
    try:
        ping = subprocess.run(["ping", "-c", "1", target], timeout=1, stdout=subprocess.DEVNULL)
        if ping.returncode == 0:
            print(colored(f"\t[i] Host {target}", 'green'))
    except subprocess.TimeoutExpired:
        pass

def main():
    target_str = get_args()
    targets = parse_target(target_str)

    print(f"\n[+] Active hosts found:")
    max_threads = 100
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(host_discovery, targets)

if __name__ == '__main__':
    main()