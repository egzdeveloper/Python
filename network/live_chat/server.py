import socket
import threading
from client_thread import ClientThread

def start_chat_server():
    host = 'localhost'
    port = 1234

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f'\n[+] Servidor en escucha...')
    conn, addr = server_socket.accept()
    print(f'\n[+] Se ha conectado el cliente {addr}')

    while True:
        message = conn.recv(1024).strip().decode()
        print(f'\n[+] Mensaje recibido: {message}')

        if message == 'bye':
            break

        server_message = input(f'\n[+] Mensaje para el cliente: ')
        conn.send(server_message.encode())

    conn.close()

start_chat_server()