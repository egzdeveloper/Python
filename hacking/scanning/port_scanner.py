import argparse
import socket
import signal
import sys
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored

open_sockets = []

def def_handler(sig, frame):
    print(colored(f"\n[!] Exiting ...", "red"))
    for sock in open_sockets:
        sock.close()

    sys.exit(1)

signal.signal(signal.SIGINT, def_handler) # Ctrl + C

def get_arguments():
    parser = argparse.ArgumentParser(description='Fast TCP Port Scanner')
    parser.add_argument("-t", "--target", required=True, dest="target", help="Target IP (Ex: -t 192.168.1.1)")
    parser.add_argument("-p", "--port", required=True, dest="port", help="Port range (Ex: -p 1-100)")
    options = parser.parse_args()

    return options.target, options.port

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    open_sockets.append(s)
    return s

def port_scanner(host, port):
    s = create_socket()

    try:
        s.connect((host, port))
        s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
        response = s.recv(1024)
        response = response.decode(errors='ignore').split('\n')[0]

        if response:
            print(colored(f"\n[+] Port {port} is open - {response}", "green"))
        else:
            print(colored(f"\n[+] Port {port} is open", "green"))

    except (socket.timeout, ConnectionRefusedError):
        pass
    finally:
        s.close()

def scan_ports(host, ports):
        with ThreadPoolExecutor(max_workers=50) as executor:
            executor.map(lambda port: port_scanner(host, port), ports)

def parse_ports(ports_str):
    if '-' in ports_str:
        start, end = map(int, ports_str.split('-'))
        return range(start, end + 1)
    elif ',' in ports_str:
        return map(int, ports_str.split(','))
    else:
        return (int(ports_str),)

def main():
    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)
    scan_ports(target, ports)

if __name__ == "__main__":
    main()