#Author: DarkAO
#Python hash generat0r. support ms5, sha versions.
#Name: HashP
import hashlib

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
    (5) EXIT
"""


while(True):
    sec = raw_input("Please select algoritms-> ")
    if sec =="5":
        break
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
        else:
            print "Unknowing command! "
