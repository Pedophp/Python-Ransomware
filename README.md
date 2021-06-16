# Introduction
This is a python based ransomware , it encryptes files with specified extensions of root or a specified path
It also fetched saved passwords in chrome and saves it in a txt file the  sends the txt file to the attacker via sockets

# Warning
ftserver.py - this script will run on the attackers computer ( it listens for connection on 0.0.0.0) keep running this script before executing any script


chromefetch.py - prints the saved passwords on the terminal(doesnt saves or sends to the host)( gives error on chrome version 80 or above but gets the job done )


chromesavepass.py - saves fetched passes to a txt file named passtxt.txt on the desktop of the victim and then sends it to the attcker via socket(change host on line 9 if not on the same network)( gives error on chrome version 80 or above but gets the job done )


login.py - same as chromefetch.py but doesnt give any error 


gen_public_private_keys.py - this is the first script you wanna run ( attacker) this genrates two asymmetric rsa keys namely public.pem and private.pem


ransomewarer.py - send this script and public.pem to the victim ( ransomwarer.py and public.pem needs to be in the same directory) !! USE A TESTING FOLDER FIRST FOR TESTING CHANGE THE PATH ON LINE 52 !! . This only encryptes ".txt" files if you wanna add more extensions edit it on line 33 This script puts a file named EMAIL_ME.txt on the victim's desktop
the victim is instructed to send this text file to an email address. When the attcker gets the EMAIL_ME.txt file he runs another script named decrypt_fernet_key.py which decryptes the EMAIL_ME.txt and outputs a PUT_ME_ON_DESKTOP.txt which when sent to victim he shall put it on his desktop which will result in decryption of the files



#FEATURES OF RANSOMEWARER.PY :
- Encryptes specified data
- Changes backgorund to a scary image (u can change imange url on line 120)
- Creates a text file named Ransome.txt in which instructions are given in order to get back the files(paying in bitcoin)( the ransome note is on line 131)
- Checks every 5 seconds if Ransome.txt is on the top window if not reopens it 
- Opens web browser in which search results of "what is bitcoin" is displayed assuming the victim doesnt know about bitcoin and how to pay
- Fetches saved chrome passwords username and their urls , saved it to a file (passtxt.txt on Desktop) , sends to the attcker
