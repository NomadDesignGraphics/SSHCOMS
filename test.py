from lib.libs import *

def ipkontrol(c_id):
    try:
        ip = ipadr.ip_address(c_id)
        print("Geçerli IP tespit edildi")
    except ValueError:
        print("Girdiğiniz ip adresi geçerli değildir")
        
ipkontrol("192.168.1.1")