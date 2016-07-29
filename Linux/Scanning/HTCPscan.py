##############################################################
#                     Half-Open TCP Scnning                  #
##############################################################
from scapy.all import *
ip = IP(src="172.16.10.1", dst ="172.16.10.130" )
tcp = TCP(sport =1024, dport=80, flags="S", seq=12345)
Spacket = ip/tcp
p = sr1(Spacket, inter=1)
p.show()

rs = TCP(sport =1024, dport=80, flags="R", seq=12347)
Rpacket = ip/rs
rp = sr1(Rpacket)
rp.show
