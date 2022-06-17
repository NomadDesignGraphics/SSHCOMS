from lib.libs import *

# def ipkontrol(c_id):
#     try:
#         ip = ipadr.ip_address(c_id)
#         print("Geçerli IP tespit edildi")
#     except ValueError:
#         print("Girdiğiniz ip adresi geçerli değildir")
        
# ipkontrol("192.168.1.1")
port=5900
yap_csv = [["ports"],]
for i in range(1000):
    port+i.append(yap_csv)

print(yap_csv)