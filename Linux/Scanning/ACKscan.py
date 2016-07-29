##############################################################
#                          ACK TCP Scnning                   #
##############################################################
from scapy.all import *
ip = IP(src="172.16.10.1", dst ="172.16.10.130")
tcp = TCP(sport =1024, dport=80, flags="A", seq=12345)
packet = ip/tcp
p =sr1(packet)
p.show()
