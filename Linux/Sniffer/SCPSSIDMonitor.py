##############################################################
#      SSID BSSID and Channel Monitor Based on Scapy         #
##############################################################
from scapy.all import *
import struct
interface = 'wlan0'
ap_list = []
def info(fm):
    if fm.haslayer(Dot11):
        if ((fm.type == 0) & (fm.subtype==8)):
            if fm.addr2 not in ap_list:
                ap_list.append(fm.addr2)
                print "SSID--> ",fm.info
                print "BSSID --> ",fm.addr2
                print "Channel--> ", ord(fm[Dot11Elt:3].info)	
				
sniff(iface=interface,prn=info)
