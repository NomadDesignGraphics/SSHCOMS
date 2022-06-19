import lib.libs 
from lib.libs import os,incele 

#SADECE WIFI MODÜLDE GEÇERLİ OLABİLİR
def Bag_tipi():
    while True:
        print("Bağlantı ngrok tanımı sağlanıyor?")
        print("PORT:4000 kontrol ediliyor")
        # soket = sok.socket(sok.AF_INET, sok.SOCK_STREAM)
        # kontrol = soket.connect_ex((cid,4000))
        kontrol = incele(4000)
        if kontrol == True:
            print("Ngrok arka planda çalıştığı tespit edildi")
            print("bağlantınızı NGROK üzerinden yürütmek istiyormusunuz")
            global yayinci
            yayinci = str(input("y/n"))
            if yayinci == 'y' or yayinci == 'Y':
                os.system("cls")
                print("Lütfen gerekli bilgileri giriniz")
                global ngrok_adres
                print("NGROK'un '#.tcp.ngrok.io' alanındaki #  kısmı: ")
                global ngrok_no
                ngrok_no = int(input(""))
                print("NGROK un 'x.tcp.ngrok.io:#####' \n kısmından sonra gelen port:(#####) numarasını: ")
                global ngrok_port
                ngrok_port = int(input(""))
            elif yayinci !='y' or yayinci !='Y':
                break