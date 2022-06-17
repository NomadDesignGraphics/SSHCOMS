from lib.libs import *

def bakport(p):
    soket = sok.socket(sok.AF_INET, sok.SOCK_STREAM)
    kontrol = kontrol.connect_ex((c_id, p))
    kontrol.close()
    return kontrol == 0

def CihazTani():
    os.system("clear")
    yorum = "Cihazı bütün bağlantı işlemlerinden önce \n tanıma işlemleri başlatılıyor... \n"
    print(yorum)
    print("Hedef cihazın 'Termux' adı alınıyor ")
    global c_ad 
    c_ad = sok.gethostname()
    
    if c_ad != "": 
        os.system("clear")
        print(yorum)
        print("Hedef cihazın 'Termux' adı: {0}".format(c_ad))
        global c_id
        c_id = sok.gethostbyname(sok.gethostname())
        print("Hedef cihazın 'IPv4' ip: {0}".format(c_id))
        if c_id != "":
            os.system("clear")
            print(yorum)
            print("Hedef cihazın 'Termux' adı: {0}".format(c_ad))
            print("Hedef cihazın 'IPv4' id: {0}".format(c_id))
            #PORT İNCELEME DÖNGÜSÜ EKLENECEK
            
            global c_prt
            c_prt = int(input(""))
        elif c_id == "":
            print("Cihaz IPv4 alınamıyor")
            print("Vaz geçiliyor...")
    elif c_ad == "":
        print("Cihaz adı alınamıyor")
        print("Vaz geçiliyor...")


def HucreselBag():
 basa_sar = True
 while basa_sar:
    basa_sar = False
    print("Hedef cihaz hangi hücresel ağ tipi kullanmaktadır?")
    hucre_bag= str(input("WIFI (1) / Mobil Veri (2) : "))
    if hucre_bag==1:
            os.system("cls")
            print("Wifi Modül seçildi")
            os.system("ssh {0}@{1} -p {2}".format(c_ad,c_id,8022))
    elif hucre_bag==2:
            os.system("cls")
            print("MV modül seçildi")
    else:
            basa_sar=True