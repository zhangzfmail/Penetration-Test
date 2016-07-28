##############################################################
#                      Ethernet Packet Craft                 #
##############################################################
import socket
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
s.bind(("vmnet10",socket.htons(0x0800)))
sor = '\x00\x0c\x29\x4f\x8e\x35'
des ='\x00\x0c\x29\x02\xd6\x2b'
code ='\x08\x00'
eth = des+sor+code
s.send(eth)
