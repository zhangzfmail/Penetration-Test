##############################################################
#       A TCP Scanning Program to Detect Live System         #
##############################################################
import socket
from datetime import datetime
#Initialize Network Address for Ping Sweeping
netaddress = raw_input("Enter the Network Address ")
netlist= netaddress.split('.')
dot = '.'
netspace = netlist[0]+dot+netlist[1]+dot+netlist[2]+dot
start = int(raw_input("Enter the Starting Number "))
end = int(raw_input("Enter the Last Number "))
end=end+1

#Record Ping Sweeping Start Time
Stime= datetime.now()

#Conduct TCP Scanning
def Scanning (address):
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    try:
        result = sock.connect_ex((address,80))
    except Exception as e:
        print("Address %s:%d, Exception is %s" % (address, port, e))
    if result==0:
        return 1
    else:
        return 0

def Running ():
    for ip in xrange(start,end):
        address = netspace+str(ip)
        if (Scanning(address)):
            print address, "--> Live"
        else:
            print address, "Not Responding"

Running()
Etime=datetime.now()
total=Etime-Stime
print "TCP Scanning Completed in ", total
