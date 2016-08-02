##############################################################
#                         Banner Grabbing                    #
##############################################################
import socket
import struct
import binascii
import re
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))

a_tag = 'HTTP'
b_tag = 'text/html'

def GBanner (content):
    for amatch in re.finditer(a_tag,content):
        s= amatch.start()
        for bmatch in re.finditer(b_tag,content):
            e = bmatch.start()
            print (content[s:e+len(b_tag)])

while True:
    try:
        pkt = s.recvfrom(2048)
        banner = pkt[0][54:533]
    except:
        print "Exception Found"
    content = str(banner)
    GBanner (content)
