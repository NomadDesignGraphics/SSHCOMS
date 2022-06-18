from lib.libs import ipadr
def ipkontrol(c_id):
    try:
        ip = ipadr.ip_address(c_id)
        print("Geçerli IP tespit edildi")
    except ValueError:
        print("Girdiğiniz ip adresi geçerli değildir")