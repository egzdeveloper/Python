import socket

def start_udp_server():
    host = "localhost"
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"\n[+]Servidor UDP iniciado en {host}:{port}")

        while True:
            data, addr = s.recvfrom(1024)
            print(f"\n[+] Mensaje del cliente: {data.decode()}")
            print(f"[+] Info del cliente: {addr}")

start_udp_server()