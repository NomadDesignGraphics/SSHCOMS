

# def ipkontrol(c_id):
#     try:
#         ip = ipadr.ip_address(c_id)
#         print("Geçerli IP tespit edildi")
#     except ValueError:
#         print("Girdiğiniz ip adresi geçerli değildir")
        
# ipkontrol("192.168.1.1")
paylasilan_port = int(input("Lütfen 59XX portundaki XX yerine geçecek sayıyı giriniz"))
global iport
iport = 5900 + paylasilan_port
print(iport)