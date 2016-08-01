##############################################################
#                 SSID BSSID and Channel Monitor             #
#Instruction:                                                #
#    sudo airmon-ng wlan0 stop                               #
#    sudo ifconfig wlan0 down                                #
#    sudo iwconfig wlan0 mode monitor                        #
#    sudo ifconfig wlan0 up                                  #
##############################################################
import socket 
import sys, os, signal
sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 3)
sniffer.bind(("mon0", 0x0003))
ap_list =[]
while True :
    #Store the Content of the Packet
    tm = sniff.recvfrom(6000)
    fm= tm[0]
    if fm[26] == "\x80":
        if fm[36:42] not in ap_list:
            ap_list.append(fm[36:42])
            #Record the Length of SSID
            length = ord(fm[63])
            print "SSID -> ",fm[64:64+length]
            print "BSSID -> ", fm[36:42].encode('hex')
            print "Channel -> ", ord(fm[64+length+12])
