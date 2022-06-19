import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import ipaddress as ipadr
import socket as sok
import csv
import bag_tipi 
import cihaz_tani
import ipcheck 
import termux_conn


#from ..bag_tipi import Bag_tipi as Bt 
#from ..ipcheck import ipkontrol as ipchk
#from ..cihaz_tani import CihazTani as ct,HucreselBag as hb,bakport as incele
__all__ = [
    'os',
    'sys',
    'ipadr',
    'csv',
    'bag_tipi',
    'ipcheck',
    'cihaz_tani',
    #'hb',
    'sok',
    #'incele',
]