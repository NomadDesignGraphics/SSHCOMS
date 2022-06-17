from lib.libs import *
from lib.globals import *

#Transfer Port To Windows
def tptw():
    if yayin == "y":
        #aktarmalı ngrok bağlantı
        os.system("ssh {0}@{1}.tcp.ngrok.io -p {2} -L {3}:localhost{3}".format(cad,nogrok,pogrok,cort))


