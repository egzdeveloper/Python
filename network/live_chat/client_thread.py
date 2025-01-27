import threading

class ClientThread(threading.Thread):
    def __init__(self, client_sock, client_addr):
        super().__init__()
        self.client_sock = client_sock
        self.client_addr = client_addr

        print(f"\n[+] Nuevo cliente conectado: {client_addr}")

    def run(self):
        while True:
            data = self.client_sock.recv(1024)
            message = data.decode()
            if message.strip() == 'bye':
                break

            print(f"\n[+] Mensaje enviado por el cliente: {message.strip()}")
            self.client_sock.send(data)

        print(f"\n[!] Cliente {self.client_addr} desconectado")
        self.client_sock.close()
            