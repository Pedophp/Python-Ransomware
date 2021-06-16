# Introduction
This is a python based ransomware , it encryptes files with specified extensions of root or a specified path
It also fetched saved passwords in chrome and saves it in a txt file the  sends the txt file to the attacker via sockets

# Warning
!! Chnage the path on line 51 to a testing folder !! change the host on line 25 the attackers ip (only works if both devices are in the same network (am working on sending over internet) !! this script only encryptes .txt files you can add more extension in file_exts on line 31

# HOW TO
- first thing run the gen_public_private_keys.py this script will generate two asymmetric rsa encryption keys namely public.pem and private.pem

- run ftserver.py (do not close until files is received )

- send the ransomewarer.py and public.pem to the victim (these 2 fiels have to be in the same directory )
 
- victim runs the ransomwarer.py ( files encryted , saved passes sent via sockets , you can exit the ftserver script )
 
- after running this script a text file named EMAIL_ME.txt fill generate on victims desktop
 
- victim have to email theis file to the attacker
 
- attacker runs decrypt_fernet_key.py (EMAIL_ME.txt and decrypt_fernet_key.py have to in the same directory)
 
- this script generates a file called PUT_ME_ON_YOUR_DESKTOP.txt on attackers computer
 
- after the victim has made the payment 
 
- attacker send PUT_ME_ON_YOUR_DESKTOP.txt to the victim 
 
- victim places this file on his desktop 
 
- files are decrypted


# FEATURES OF RANSOMEWARER.PY :
- Encryptes specified data
- Changes backgorund to a specified image (u can change imange url on line 120)
- Creates a text file named Ransome.txt in which instructions are given in order to get back the files(paying in bitcoin)( the ransome note is on line 131)
- Checks every 5 seconds if Ransome.txt is on the top window if not reopens it 
- Opens web browser in which search results of "what is bitcoin" is displayed assuming the victim doesnt know about bitcoin and how to pay
- Fetches saved chrome passwords username and their urls , saved it to a file (passtxt.txt on Desktop) , sends to the attcker

# HOT TO RUN RANSOMEWARE ON WINDOWS WITHOUT PYTHON
- install pyinstaller (pip install pyinstaller)

- pyinstaller --onefile rasomewarer.py
- open the dist folder which was made move the exe file to the same directory as the public.pem file
- send the ransomwarer.exe to the victim file along with the python and public.pem file
- you can search for tutorials on yt for python to exe 
