import socket
import threading as th
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import ssl

def send_message(client_socket, username, text_widget, entry_widget):
    message = entry_widget.get()
    client_socket.sendall(f"{username} > {message}".encode())
    entry_widget.delete(0, END)
    text_widget.configure(state=NORMAL)
    text_widget.insert(END, f"{username} > {message}\n")
    text_widget.configure(state=DISABLED)

def receive_message(client_socket, text_widget):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                text_widget.configure(state=NORMAL)
                text_widget.insert(END, message)
                text_widget.configure(state=DISABLED)
            else:
                break
        except:
            break

def list_users(client_socket):
    client_socket.sendall("!users".encode())

def exit(client_socket, username, window):
    client_socket.sendall(f"\n[!] User {username} exit the chat\n".encode())
    client_socket.close()
    window.quit()
    window.destroy()

def client_program():
    host = "localhost"
    port = 1234
    username = input(f"\n[+] Enter username: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket = ssl.wrap_socket(client_socket)
    client_socket.connect((host, port))
    client_socket.sendall(username.encode())

    window = Tk()
    window.title("Realtime Chat")

    text_widget = ScrolledText(window, state=DISABLED)
    text_widget.pack(padx=5, pady=5)

    frame_widget = Frame(window)
    frame_widget.pack(padx=5, pady=5, fill=BOTH, expand=1)

    entry_widget = Entry(frame_widget, font=("Arial", 15))
    entry_widget.bind("<Return>", lambda _: send_message(client_socket, username, text_widget, entry_widget))
    entry_widget.pack(side=LEFT, fill=BOTH, expand=1)

    button_widget = Button(frame_widget, text="Send", command=lambda: send_message(client_socket, username, text_widget, entry_widget))
    button_widget.pack(side=RIGHT, padx=5)

    users_widget = Button(window, text="Users", command=lambda: list_users(client_socket))
    users_widget.pack(padx=5, pady=5)
    exit_widget = Button(window, text="Exit", command=lambda: exit(client_socket, username, window))
    exit_widget.pack(padx=5, pady=5)

    thread = th.Thread(target=receive_message, args=(client_socket, text_widget))
    thread.daemon = True
    thread.start()

    window.mainloop()
    client_socket.close()

if __name__ == "__main__":
    client_program()