from lib.libs import os
from lib.globals import yayin,cad,cid,cort,nogrok,pogrok

#Transfer Port To Windows for TCP connection
def tptw():
    basa_sar = True
    while(basa_sar):
        basa_sar = False
        global paylasilan_port
        paylasilan_port = int(input("Lütfen TCP bağ için 59XX portundaki XX yerine geçecek sayıyı giriniz (1-99)"))
        if paylasilan_port >= 100 or paylasilan_port <= 0:
            print("Lütfen 1 ile 99 dahil olacak şekilde aralarında kalan sayılardan giriş yapınız")
            basa_sar = True
        
    global iport
    iport = 5900 + paylasilan_port
    if yayin == "y" or yayin == "Y":
        #aktarmalı ngrok bağlantı
        os.system("ssh {0}@{1}.tcp.ngrok.io -p {2} -L {3}:localhost{3}".format(cad,nogrok,pogrok,iport))
    
    elif yayin != "y" or yayin != "Y":
        
        os.system("ssh {0}@{1} -p {2} -L {3}:localhost:{3}".format(cad,cid,cort,iport))

