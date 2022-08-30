#! /usr/bin/env python3
from colorama import init, Fore, Back, Style
banner="""

 ▄▀▀▄ ▄▄   ▄▀▄▄▄▄   ▄▀▀▄ ▄▀▄                                                 
█  █   ▄▀ █ █    ▌ █  █ ▀  █ 
▐  █▄▄▄█  ▐ █      ▐  █    █     
███████████  ███                 █████                   
░░███░░░░░░█ ░░                ░░███                    
 ░███   █ ░  ████  ████████    ███████   ██████  ████████ 
 ░███████   ░░███ ░░███░░███  ███░░███  ███░░███░░███░░███   
 ░███░░░█    ░███  ░███ ░███ ░███ ░███ ░███████  ░███ ░░░                        
 ░███  ░     ░███  ░███ ░███ ░███ ░███ ░███░░░   ░███     
 █████       █████ ████ █████░░████████░░██████  █████    
░░░░░       ░░░░░ ░░░░ ░░░░░  ░░░░░░░░  ░░░░░░  ░░░░░   
   █   █    █        █    █  
  ▄▀  ▄▀   ▄▀▄▄▄▄▀ ▄▀   ▄▀   
 █   █    █     ▐  █    █    
 ▐   ▐    ▐        ▐    ▐       v1.0         
                                                                                                                          
                                                                                                                                                             
███╗   ███╗ █████╗ ██████╗ ███████╗    ██████╗ ██╗   ██╗     ██████╗██╗   ██╗██████╗ ███████╗██████╗     ███████╗ ██████╗ ██╗     ██████╗ ██╗███████╗██████╗ 
████╗ ████║██╔══██╗██╔══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝    ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗    ██╔════╝██╔═══██╗██║     ██╔══██╗██║██╔════╝██╔══██╗
██╔████╔██║███████║██║  ██║█████╗      ██████╔╝ ╚████╔╝     ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝    ███████╗██║   ██║██║     ██║  ██║██║█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║  ██║██╔══╝      ██╔══██╗  ╚██╔╝      ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗    ╚════██║██║   ██║██║     ██║  ██║██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║██████╔╝███████╗    ██████╔╝   ██║       ╚██████╗   ██║   ██████╔╝███████╗██║  ██║    ███████║╚██████╔╝███████╗██████╔╝██║███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝    ╚═════╝    ╚═╝        ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚══════╝╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝
"""
print(banner)
print("note the script is case-sensitive and use grep for more easily to find what do u want and use the name or number  of the hash"  )
print ("""
1-MD5               
2-md5($pass.$salt) 
3-md5($salt.$pass)
4-md5(utf16le($pass).$salt)
5-md5($salt.utf16le($pass)) 
6-HMAC-MD5 (key = $pass) 
7-HMAC-MD5 (key = $salt)
8-md5(utf16le($pass))
9-SHA1
10-sha1($pass.$salt)
11-sha1($salt.$pass)  
12-sha1(utf16le($pass).$salt)
13-sha1($salt.utf16le($pass))
14-HMAC-SHA1 (key = $pass)
15-HMAC-SHA1 (key = $salt)
16-sha1(utf16le($pass))
17-MySQL323
18-MySQL4.1/MySQL5
19-phpass, WordPress (MD5),Joomla (MD5)
20-phpass, phpBB3 (MD5)
21-md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5)^2
22-Juniper IVE
23-BLAKE2b-512
24-BLAKE2b-512($pass.$salt) *
25-BLAKE2b-512($salt.$pass)
26-MD4
27-NTLM
28-Domain Cached Credentials (DCC), MS Cache
29-SHA2-224
30-SHA2-256
31-sha256($pass.$salt)
32-sha256($salt.$pass)
33-sha256(utf16le($pass).$salt)
34-sha256($salt.utf16le($pass))
35-HMAC-SHA256 (key = $pass)
36-HMAC-SHA256 (key = $salt)
37-sha256(utf16le($pass))
38-descrypt, DES (Unix), Traditional DES
39-Apache $apr1$ MD5, md5apr1, MD5 (APR) 2
40-SHA2-512
""")#menu
hash=input("Please Enter hash type to find its mode or select from the menu\n")#hash



if (hash == 'MD5') |  (hash == '1') : 
      print('\033[31m'+"your mode is 0")
if (hash == 'md5($pass.$salt)') | (hash =='md5($pass.$salt)')| (hash == '2') : 
      print('\033[31m'+"your mode is 10")
if (hash == 'md5($salt.$pass)') | (hash =='3'):
        print('\033[31m'+"your mode is 20")
if (hash == 'md5(utf16le($pass).$salt)') | (hash =='4'):
        print('\033[31m'+"your mode is 30")
if (hash =='md5($salt.utf16le($pass))') | (hash=='5'):
     print('\033[31m'+"your mode is 40")
if (hash =='HMAC-MD5 (key = $pass)') | (hash=='6'):
        print('\033[31m'+'your mode is 50')
if (hash == 'HMAC-MD5 (key = $salt)') | (hash=='7'):
        print('\033[31m'+"your mdoe is 60")
if (hash =='md5(utf16le($pass))') | (hash=='8'):
        print('\033[31m'+"your mdoe is 70")
if (hash =='SHA1') | (hash =='9') :
        print('\033[31m'+'your mode is 100')
if (hash=='sha1($pass.$salt)') | (hash =='10') :
        print('\033[31m'+"your mode is 110 ")
if (hash =='sha1($salt.$pass)') | (hash =='11'):
        print ('\033[31m'+"your mode is 120 ")
if (hash =='sha1(utf16le($pass).$salt)') | (hash =='12'):
        print ('\033[31m'+"your mode is 130 ")
if (hash =='sha1($salt.utf16le($pass))') | (hash =='13'):
        print ('\033[31m'+"your mode is 140 ")
if (hash =='HMAC-SHA1 (key = $pass)') | (hash =='14'):
        print ('\033[31m'+"your mode is 150 ")
if (hash =='HMAC-SHA1 (key = $salt) ') | (hash =='15'):
        print ('\033[31m'+"your mode is 160 ")
if (hash =='sha1(utf16le($pass))') | (hash =='16'):
        print ('\033[31m'+"your mode is 170 ")
if (hash =='MySQL323') | (hash =='17'):
        print ('\033[31m'+"your mode is 200 ")
if (hash=='MySQL4.1/MySQL5') | (hash=='18') :
        print ('\033[31m'+"your mode is 300 ")
if (hash=='phpass, WordPress (MD5),Joomla (MD5)') | (hash=='19') :
        print ('\033[31m'+"your mode is 400 ")
if (hash=='phpass, phpBB3 (MD5)') | (hash=='20') :
        print ('\033[31m'+"your mode is 400 ")
if (hash=="md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5)^2") | (hash=='21'):
        print ('\033[31m'+"your mode is 500 ")
if (hash=="Juniper IVE") | (hash=='22'):
        print ('\033[31m'+"your mode is 501 ")
if (hash=="BLAKE2b-512") | (hash=='23'):
        print ('\033[31m'+"your mode is 600 ")
if (hash =='BLAKE2b-512($pass.$salt) *') | (hash =='24') : 
       print ('\033[31m'+"your mode is  610")
if (hash ==' BLAKE2b-512($salt.$pass) *') | (hash =='25') : 
       print ('\033[31m'+"your mode is  620")
if (hash =='MD4') | (hash =='26') : 
       print ('\033[31m'+"your mode is  900")
if (hash =='NTLM') | (hash =='27') : 
       print ('\033[31m'+"your mode is 1000")
if (hash =='Domain Cached Credentials (DCC), MS Cache') | (hash =='28') : 
       print ('\033[31m'+"your mode is 1100 ")
if (hash =='SHA2-224') | (hash =='29') : 
       print ('\033[31m'+"your mode is 1300 ")
if (hash =='SHA2-256') | (hash =='30') : 
       print ('\033[31m'+"your mode is 1400")
if (hash =='sha256($pass.$salt)') | (hash =='31') : 
       print ('\033[31m'+"your mode is 1410 ")
if (hash =='sha256($salt.$pass)') | (hash =='32') : 
       print ('\033[31m'+"your mode is 1420")
if (hash =='sha256(utf16le($pass).$salt)') | (hash =='33') : 
       print ('\033[31m'+"your mode is 1430")
if (hash =='sha256($salt.utf16le($pass))') | (hash =='34') : 
       print ('\033[31m'+"your mode is 1440")
if (hash =='HMAC-SHA256 (key = $pass)') | (hash =='35') : 
       print ('\033[31m'+"your mode is 1450")
if (hash =='HMAC-SHA256 (key = $salt)') | (hash =='36') : 
       print ('\033[31m'+"your mode is 1460")
if (hash =='sha256(utf16le($pass))') | (hash =='37') : 
       print ('\033[31m'+"your mode is 1470")
if (hash =='descrypt, DES (Unix), Traditional DES') | (hash =='38') : 
       print ('\033[31m'+"your mode is 1500")
if (hash =='Apache $apr1$ MD5, md5apr1, MD5 (APR) 2') | (hash =='39') : 
       print ('\033[31m'+"your mode is 1600")
if (hash =='SHA2-512') | (hash =='40') : 
       print ('\033[31m'+"your mode is 1700")











