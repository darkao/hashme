#!/usr/bin/python
#Author: Xr00tgh0st
#Python hash generat0r. support md5, sha versions.
#Name: HashP

import hashlib
import base64
import os


def md5():
    global al
    m = hashlib.md5(al)
    print al+" = "+m.hexdigest()

def sha1():
    global al
    m = hashlib.sha1(al)
    print al + " = "+m.hexdigest()

def sha256():
    global al
    m = hashlib.sha256(al)
    print al + " = " +m.hexdigest()

def sha512():
    global al
    m = hashlib.sha512(al)
    print al + " = "+m.hexdigest()
    
def base():
    global al
    b = base64.b64encode(al)
    print b

def base_d():
    global al
    b = base64.b64decode(al)
    print b

def banner():
    print """
 _     _            _         ______                                 
| |   | |          | |       / _____)                _               
| |__ | | ____  ___| | _    | /       ____ ____ ____| |_  ___   ____ 
|  __)| |/ _  |/___) || \   | |      / ___) _  ) _  |  _)/ _ \ / ___)
| |   | ( ( | |___ | | | |  | \_____| |  ( (/ ( ( | | |_| |_| | |    
|_|   |_|\_||_(___/|_| |_|   \______)_|   \____)_||_|\___)___/|_| Xr00tgh0st

                                                                     """

banner()
print """
    (1) MD5
    (2) SHA1
    (3) SHA256
    (4) SHA512
    (5) BASE64
    (6) TO EXIT
"""


while(True):
    sec = raw_input("Please select algoritms-> ")
    
    if sec == "6":
        print "Game Over, good byee!"
        exit()
    
    al = raw_input("-> ")

    if sec =="" or al == "":
        print "Please don't fill in the fields"
    else:
        if sec == "1":
            md5()
        elif sec == "2":
            sha1()
        elif sec == "3":
            sha256()
        elif sec == "4":
            sha512()
        elif sec == "5":
            sor = raw_input("""
    (1) ENCODE
    (2) DECODE
-> """)
            if sor == "":
                    print "Please don't fill in the fields"
            else:
                if sor == "1":
                    base()
                elif sor == "2":
                    base_d()
                else:
                    print "Unknowing command! "
        else:
            print "Unknowing command! "

