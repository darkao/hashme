#python 3 version
import hashlib
import base64
import os

def md5():
    global key
    m = hashlib.md5(str.encode(key))
    print(key+" = "+m.hexdigest())

def sha1():
    global key
    m = hashlib.sha1(str.encode(key))
    print(key+" = "+m.hexdigest())

def sha256():
    global key
    m = hashlib.sha256(str.encode(key))
    print(key+" = "+m.hexdigest())

def base():
    global key
    b = base64.b64encode(key.encode("utf-8", "ignore"))
    print(b)

def base_d():
    global key
    b_bytes = key.encode('ascii')
    key_bytes = base64.b64decode(b_bytes)
    b = key_bytes.decode('ascii')
    print(b)

def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)) == s
    except Exception:
        print("It isn't base64")
        exit()


def banner():
    print ("""
 _     _            _         ______                                 
| |   | |          | |       / _____)                _               
| |__ | | ____  ___| | _    | /       ____ ____ ____| |_  ___   ____ 
|  __)| |/ _  |/___) || \   | |      / ___) _  ) _  |  _)/ _ \ / ___)
| |   | ( ( | |___ | | | |  | \_____| |  ( (/ ( ( | | |_| |_| | |    
|_|   |_|\_||_(___/|_| |_|   \______)_|   \____)_||_|\___)___/|_| Xr00tgh0st
                                                                     """)

banner()

print("""
    (1) MD5
    (2) SHA1
    (3) SHA256
    (4) BASE64
    (5) TO EXIT
""")

while True:
    select = input("Please select algorithms-> ")
    if select == "5":
        print("See u later.")
        exit()


    if select == "":
        print("Please don't fill in the fields")
    else:
        if select == "1":
            key = input("-> ")
            if key == "":
                print("Please don't fill in the fields")
            else:
                md5()
        elif select == "2":
            key = input("-> ")
            if key == "":
                print("Please don't fill in the fields")
            else:
                sha1()
        elif select == "3":
            key = input("-> ")
            if key == "":
                print("Please don't fill in the fields")
            else:
                sha256()
        elif select == "4":
            get = input("""
(1) ENCODE
(2) DECODE
            ->""")
            if get == "":
                print("Please don't fill in the fields")
            else:
                if get == "1":
                    key = input("-> ")
                    if key == "":
                        print("Please don't fill in the fields")
                    else:
                        base()
                elif get == "2":
                    key = input ("->")
                    isBase64(key)
                    if key == "":
                        print("Please don't fill in the fields")
                    else:
                        base_d()
                else:
                    print("Unknowing command!")
        else:
            print("Unknowing command!")
