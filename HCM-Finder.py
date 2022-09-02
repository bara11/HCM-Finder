#! /usr/bin/env python3
from colorama import init, Fore, Back, Style
import os
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
print("note: the script is case-sensitive and use grep for more easily to find what do u want and use the name or number  of the hash " )
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
21-md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5)
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
41-sha512($pass.$salt)
42-sha512($salt.$pass)
43-sha512(utf16le($pass).$salt)
44-sha512($salt.utf16le($pass))
45-HMAC-SHA512 (key = $pass)
46-HMAC-SHA512 (key = $salt)
47-sha512(utf16le($pass))
48-sha512crypt $6$, SHA512 (Unix)
49-STDOUT
50-Domain Cached Credentials 2 (DCC2), MS Cache 2
51-Cisco-PIX MD5
52-Cisco-ASA MD5
53-WPA-EAPOL-PBKDF2
54-WPA-EAPOL-PMK
55-md5(md5($pass))
56-LM
57-Oracle H: Type (Oracle 7+)
58-bcrypt $2*$, Blowfish (Unix)
59-md5(md5(md5($pass)))
60-md5($salt.md5($pass))
61-md5($salt.$pass.$salt)
62-md5(md5($pass).md5($salt))
63-md5($salt.md5($salt.$pass))
64-md5($salt.md5($pass.$salt))
65-md5(strtoupper(md5($pass)))
66-md5(sha1($pass))
67-md5(sha1($pass).$salt)
68-sha1(sha1($pass))
69-sha1(sha1($pass).$salt)
70-sha1($salt.sha1($pass))
71-sha1(md5($pass))
72-sha1(md5($pass).$salt)
73-iSCSI CHAP authentication, MD5(CHAP)
74-sha1($salt.$pass.$salt)
75-sha1(sha1($salt.$pass.$salt))
76-Half MD5
77-Password Safe v3
78-IKE-PSK MD5
79-IKE-PSK SHA1
80-NetNTLMv1 / NetNTLMv1+ESS
81-NetNTLMv2
82-Cisco-IOS type 4 (SHA256)
83-Samsung Android Password/PIN
84-RIPEMD-160
85-Whirlpool
86-TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + AES (legacy)
87-TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Serpent (legacy)
88-TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Twofish (legacy)
89-TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + AES-Twofish (legacy)
90-TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + AES-Twofish-Serpent (legacy)
91-TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Serpent-AES (legacy)
92-TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Serpent-Twofish-AES (legacy)
93-TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Twofish-Serpent (legacy)
94-TrueCrypt 5.0+ SHA512 + AES (legacy)
95-TrueCrypt 5.0+ SHA512 + Serpent (legacy)
96-TrueCrypt 5.0+ SHA512 + Twofish (legacy)
97-TrueCrypt 5.0+ SHA512 + AES-Twofish (legacy)
98-TrueCrypt 5.0+ SHA512 + AES-Twofish-Serpent (legacy)
99-TrueCrypt 5.0+ SHA512 + Serpent-AES (legacy)
100-TrueCrypt 5.0+ SHA512 + Serpent-Twofish-AES (legacy)
press 0 to continue
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
if (hash=="md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5)") | (hash=='21'):
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
if (hash =='sha512($pass.$salt)') | (hash =='41') : 
       print ('\033[31m'+"your mode is 1710")
if (hash =='sha512($salt.$pass)') | (hash =='42') : 
       print ('\033[31m'+"your mode is 1720")
if (hash =='sha512(utf16le($pass).$salt)') | (hash =='43') : 
       print ('\033[31m'+"your mode is 1730")
if (hash =='sha512($salt.utf16le($pass))') | (hash =='44') : 
       print ('\033[31m'+"your mode is 1740")
if (hash =='HMAC-SHA512 (key = $pass)') | (hash =='45') : 
       print ('\033[31m'+"your mode is 1750")
if (hash =='HMAC-SHA512 (key = $salt)') | (hash =='46') : 
       print ('\033[31m'+"your mode is 1760")
if (hash =='sha512(utf16le($pass))') | (hash =='47') : 
       print ('\033[31m'+"your mode is 1770")
if (hash =='sha512crypt $6$, SHA512 (Unix)') | (hash =='48') : 
       print ('\033[31m'+"your mode is 1800")
if (hash =='STDOUT') | (hash =='49') : 
       print ('\033[31m'+"your mode is  2000")
if (hash =='Domain Cached Credentials 2 (DCC2), MS Cache 2') | (hash =='50') : 
       print ('\033[31m'+"your mode is  2100")
if (hash=='Cisco-PIX MD5') | (hash=='51'):
       print ('\033[31m'+"your mode is  2400")
if (hash=='Cisco-ASA MD5') | (hash=='52'):
       print ('\033[31m'+"your mode is  2410")
if (hash=='WPA-EAPOL-PBKDF2') | (hash=='53'):
       print ('\033[31m'+"your mode is 2500")
if (hash=='WPA-EAPOL-PMK') | (hash=='54'):
       print ('\033[31m'+"your mode is 2501")
if (hash=='md5(md5($pass))') | (hash=='55'):
       print ('\033[31m'+"your mode is 2600")
if (hash=='LM') | (hash=='56'):
       print ('\033[31m'+"your mode is 3000")
if (hash=='Oracle H: Type (Oracle 7+)') | (hash=='57'):
       print ('\033[31m'+"your mode is 3000")
if (hash=='bcrypt $2*$, Blowfish (Unix)') | (hash=='58'):
       print ('\033[31m'+"your mode is 3200")
if (hash=='md5(md5(md5($pass)))') | (hash=='59'):
       print ('\033[31m'+"your mode is 3500")
if (hash=='md5($salt.md5($pass))') | (hash=='60'):
       print ('\033[31m'+"your mode is 3710")
if (hash=='md5($salt.$pass.$salt)') | (hash=='61'):
       print ('\033[31m'+"your mode is 3800")
if (hash=='md5(md5($pass).md5($salt))') | (hash=='62'):
       print ('\033[31m'+"your mode is 3910")
if (hash=='md5($salt.md5($salt.$pass))') | (hash=='63'): 
       print ('\033[31m'+"your mode is 4010")
if (hash=='md5($salt.md5($pass.$salt))') | (hash=='64'): 
       print ('\033[31m'+"your mode is 4110")
if (hash=='md5(strtoupper(md5($pass)))') | (hash=='65'): 
       print ('\033[31m'+"your mode is 4300")
if (hash=='md5(sha1($pass))') | (hash=='66'):  
       print ('\033[31m'+"your mode is 4400")
if (hash=='md5(sha1($pass).$salt)') | (hash=='67'):  
       print ('\033[31m'+"your mode is 4410")
if (hash=='sha1(sha1($pass))') | (hash=='68'):  
       print ('\033[31m'+"your mode is 4500")
if (hash=='sha1(sha1($pass).$salt)') | (hash=='69'):  
       print ('\033[31m'+"your mode is 4510")
if (hash=='sha1($salt.sha1($pass))') | (hash=='70'):  
       print ('\033[31m'+"your mode is 4520")
if (hash=='sha1(md5($pass))') | (hash=='71'):  
       print ('\033[31m'+"your mode is 4700")
if (hash=='sha1(md5($pass).$salt)') | (hash=='72'):  
       print ('\033[31m'+"your mode is 4710")
if (hash=='iSCSI CHAP authentication, MD5(CHAP)') | (hash=='73'):  
       print ('\033[31m'+"your mode is 4800")
if (hash=='sha1($salt.$pass.$salt)') | (hash=='74'):  
       print ('\033[31m'+"your mode is 4900")
if (hash=='sha1(sha1($salt.$pass.$salt))') | (hash=='75'):  
       print ('\033[31m'+"your mode is 5000")
if (hash=='Half MD5') | (hash=='76'):  
       print ('\033[31m'+"your mode is 5100")
if (hash=='Password Safe v3') | (hash=='77'):  
       print ('\033[31m'+"your mode is 5200")
if (hash=='IKE-PSK MD5') | (hash=='78'):   
       print ('\033[31m'+"your mode is 5300")
if (hash=='IKE-PSK SHA1 ') | (hash=='79'):   
       print ('\033[31m'+"your mode is 5400")
if (hash=='NetNTLMv1 / NetNTLMv1+ESS') | (hash=='80'):   
       print ('\033[31m'+"your mode is 5500")
if (hash=='NetNTLMv2') | (hash=='81'):  
       print ('\033[31m'+"your mode is 5600")
if (hash=='Cisco-IOS type 4 (SHA256)') | (hash=='82'):  
       print ('\033[31m'+"your mode is 5700")
if (hash=='Samsung Android Password/PIN') | (hash=='83'):  
       print ('\033[31m'+"your mode is 5800")
if (hash=='RIPEMD-160') | (hash=='84'):  
       print ('\033[31m'+"your mode is 6000")
if (hash=='Whirlpool') | (hash=='85'):  
       print ('\033[31m'+"your mode is 6100")
if (hash=='TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + AES (legacy)') | (hash=='86'):  
       print ('\033[31m'+"your mode is 6211")
if (hash=='TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Serpent (legacy)') | (hash=='87'):  
       print ('\033[31m'+"your mode is 6211")
if (hash=='TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Twofish (legacy)') | (hash=='88'):  
       print ('\033[31m'+"your mode is 6211")
if (hash=='TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + AES-Twofish (legacy)') | (hash=='89'):  
       print ('\033[31m'+"your mode is 6212")
if (hash=='TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + AES-Twofish-Serpent (legacy)') | (hash=='90'):  
       print ('\033[31m'+"your mode is 6213")
if (hash=='TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Serpent-AES (legacy)') | (hash=='91'):  
       print ('\033[31m'+"your mode is 6212")
if (hash=='TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Serpent-Twofish-AES (legacy)') | (hash=='92'):  
       print ('\033[31m'+"your mode is 6213")
if (hash=='TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Twofish-Serpent (legacy)') | (hash=='93'):  
       print ('\033[31m'+"your mode is 6212")
if (hash=='TrueCrypt 5.0+ SHA512 + AES (legacy)') | (hash=='94'):  
       print ('\033[31m'+"your mode is 6221")
if (hash=='TrueCrypt 5.0+ SHA512 + Serpent (legacy)') | (hash=='95'):  
       print ('\033[31m'+"your mode is 6221")
if (hash=='TrueCrypt 5.0+ SHA512 + Twofish (legacy)') | (hash=='96'):  
       print ('\033[31m'+"your mode is 6221")
if (hash=='TrueCrypt 5.0+ SHA512 + AES-Twofish (legacy)') | (hash=='97'):  
       print ('\033[31m'+"your mode is 6222")
if (hash=='TrueCrypt 5.0+ SHA512 + AES-Twofish-Serpent (legacy)') | (hash=='98'):  
       print ('\033[31m'+"your mode is 6223")
if (hash=='TrueCrypt 5.0+ SHA512 + Serpent-AES (legacy)') | (hash=='99'):  
       print ('\033[31m'+"your mode is 6222")
if (hash=='TrueCrypt 5.0+ SHA512 + Serpent-Twofish-AES (legacy)') | (hash=='100'):  
       print ('\033[31m'+"your mode is 6223")
if (hash=='0') :
   os.system("clear")
   print("""101-TrueCrypt 5.0+ Whirlpool + AES (legacy)
102-TrueCrypt 5.0+ Whirlpool + Serpent (legacy)
103-TrueCrypt 5.0+ Whirlpool + Twofish (legacy)
104-TrueCrypt 5.0+ Whirlpool + AES-Twofish (legacy)
105-TrueCrypt 5.0+ Whirlpool + AES-Twofish-Serpent (legacy)
106-TrueCrypt 5.0+ Whirlpool + Serpent-AES (legacy)
107-TrueCrypt 5.0+ Whirlpool + Serpent-Twofish-AES (legacy)
108-TrueCrypt 5.0+ Whirlpool + Twofish-Serpent (legacy)
109-TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + AES + boot (legacy)
110-TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Serpent + boot (legacy)
111-TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + AES-Twofish + boot (legacy)
112-TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + AES-Twofish-Serpent + boot (legacy)
113-TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Serpent-AES + boot (legacy)
114-TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Serpent-Twofish-AES + boot (legacy)
115-TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Twofish-Serpent + boot (legacy)
116-AIX {smd5}
117-AIX {ssha256}
118-AIX {ssha512}

 """)
hash2=input("Please Enter hash type to find its mode or select from the menu\n")#hash2



if (hash2=='TrueCrypt 5.0+ Whirlpool + AES (legacy)') | (hash2=='101'):  
       print ('\033[31m'+"your mode is 6231")
if (hash2=='TrueCrypt 5.0+ Whirlpool + Serpent (legacy)') | (hash2=='102'):  
       print ('\033[31m'+"your mode is 6231")
if (hash2=='TrueCrypt 5.0+ Whirlpool + Twofish (legacy)') | (hash2=='103'):  
       print ('\033[31m'+"your mode is 6231")
if (hash2=='TrueCrypt 5.0+ Whirlpool + AES-Twofish (legacy)') | (hash2=='104'):  
       print ('\033[31m'+"your mode is 6232")
if (hash2=='TrueCrypt 5.0+ Whirlpool + AES-Twofish-Serpent (legacy)') | (hash2=='105'):  
       print ('\033[31m'+"your mode is  6233 ")
if (hash2=='TrueCrypt 5.0+ Whirlpool + Serpent-AES (legacy)') | (hash2=='106'):  
       print ('\033[31m'+"your mode is  6232 ")
if (hash2=='TrueCrypt 5.0+ Whirlpool + Serpent-Twofish-AES (legacy)') | (hash2=='107'):  
       print ('\033[31m'+"your mode is  6233 ")
if (hash2=='TrueCrypt 5.0+ Whirlpool + Twofish-Serpent (legacy)') | (hash2=='108'):  
       print ('\033[31m'+"your mode is  6232 ")
if (hash2=='TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + AES + boot (legacy)') | (hash2=='109'):  
       print ('\033[31m'+"your mode is  6241 ")
if (hash2=='TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Serpent + boot (legacy)') | (hash2=='110'):  
       print ('\033[31m'+"your mode is  6241 ")
if (hash2=='TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + AES-Twofish + boot (legacy)') | (hash2=='111'):  
       print ('\033[31m'+"your mode is  6242 ")
if (hash2=='TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + AES-Twofish-Serpent + boot (legacy)') | (hash2=='112'):  
       print ('\033[31m'+"your mode is  6243 ")
if (hash2=='TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Serpent-AES + boot (legacy)') | (hash2=='113'):  
       print ('\033[31m'+"your mode is  6242 ")
if (hash2=='TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Serpent-Twofish-AES + boot (legacy)') | (hash2=='114'):  
       print ('\033[31m'+"your mode is  6243 ")
if (hash2=='TrueCrypt 5.0+ PBKDF2-HMAC-RIPEMD160 + Twofish-Serpent + boot (legacy)') | (hash2=='115'):  
       print ('\033[31m'+"your mode is  6242 ")
if (hash2=="AIX {smd5}") | (hash2=='116'):  
       print ('\033[31m'+"your mode is  6300 ")
if (hash2=="AIX {ssha256}") | (hash2=='117'):  
       print ('\033[31m'+"your mode is  6400 ")
if (hash2=="AIX {ssha512}") | (hash2=='118') :
       print ('\033[31m'+"your mode is  6500 ")









