from lib.libs import *

def bag_tipi():
    while True:
        print("Bağlantı ngrok tanımı sağlanıyor?")
        global yayinci
        yayinci = str(input("y/n"))
        if yayinci == 'y' or yayinci == 'Y':
            global ngrok_adres
            print("NGROK'un 'x.tcp.ngrok.io' alanındaki x  kısmını yaz: ")
            ngrok_no = int(input(""))
            print("NGROK un 'x.tcp.ngrok.io:' \n kısmından sonra gelen port numarasını yaz: ")
            ngrok_port = int(input(""))
            ngrok_adres = "{0}.tcp.ngrok.io:{1}",ngrok_no,ngrok_port
        elif yayinci !='y' or yayinci !='Y':
            break