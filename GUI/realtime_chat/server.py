import socket
import ssl
import threading as th

def client_thread(client_socket, clients, usernames):
    username = client_socket.recv(1024).decode()
    usernames[client_socket] = username

    for client in clients:
        if client is not client_socket:
            client.sendall(f"\n[+] The user {username} has been enter in the chat\n".encode())

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            if message == "!users":
                client_socket.sendall(f"\n[+] Users connected: {', '.join(usernames.values())}\n".encode())
                continue

            for client in clients:
                if client is not client_socket:
                    client.sendall(f"{message}\n".encode())
        except:
            break

    client_socket.close()
    clients.remove(client_socket)
    del usernames[client_socket]

def server_program():
    host = "localhost"
    port = 1234

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket = ssl.wrap_socket(server_socket, keyfile="server-key.key", certfile="server-cert.crt", server_side=True)
    server_socket.listen()
    print(f"\n[+] Listening on {host}:{port}")

    clients = []
    usernames = {}

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f"\n[+] Accepted connection from {client_address}")

        thread = th.Thread(target=client_thread, args=(client_socket, clients, usernames))
        thread.daemon = True
        thread.start()

if __name__ == '__main__':
    server_program()
