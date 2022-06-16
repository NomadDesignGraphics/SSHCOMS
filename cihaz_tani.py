from lib.libs import *
def CihazTani():
    os.system("clear")
    yorum = "Cihazı bütün bağlantı işlemlerinden önce \n tanıma işlemleri başlatılıyor... \n"
    print("Hedef cihazın 'Termux' adını gir ")
    global c_ad 
    c_ad = sok.gethostname()
    
    if c_ad != "": 
        os.system("clear")
        print(yorum)
        print("Hedef cihazın 'Termux' adı: {0}", c_ad)
        print("Hedef cihazın 'TCP/Local' id: ")
        global c_id
        c_id = sok.gethostbyname(sok.gethostname())
        if c_id != "":
            os.system("clear")
            print(yorum)
            print("Hedef cihazın 'Termux' adı: {0}", c_ad)
            print("Hedef cihazın 'TCP/Local' id: {0}", c_id)
            global c_prt
            c_prt = int(input(""))


def HucreselBag():
 basa_sar = True
 while basa_sar:
    basa_sar = False
    print("Hedef cihaz hangi hücresel ağ tipi kullanmaktadır?")
    hucre_bag= str(input("WIFI (1) / Mobil Veri (2) : "))
    if hucre_bag==1:
            os.system("cls")
            print("Wifi Modül seçildi")
            os.system("ssh "+c_ad+"@"+c_id+" -p 8022")
    elif hucre_bag==2:
            os.system("cls")
            print("MV modül seçildi")
    else:
            basa_sar=True