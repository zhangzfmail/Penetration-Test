##############################################################
#      A Port Scanning Program to Detect Live System         #
##############################################################
import socket, subprocess,sys
from datetime import datetime

subprocess.call('clear',shell=True)
netaddress = raw_input("Enter the Remote Host IP to Scan: ")
sPort = int(raw_input("Enter the Starting Port Number: "))
ePort = int(raw_input("Enter the Ending Port Number: "))
print "#"*40
print "\n"
print "Port Scanning is Running on ",netaddress
print "\n"
print "#"*40

Stime= datetime.now()
try:
    for port in range(sPort,ePort):
        sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((netaddress,port))
        if result==0:
            print "Port Open:-->\t", port
        sock.close()

except KeyboardInterrupt:
    print "Scanning is Stopped by Keyboard Interrupt"
    sys.exit()

except socket.gaierror:
    print "Hostname Could not be Resolved"
    sys.exit()

except socket.error:
    print "Server Could not be Connected"
    sys.exit()

Etime= datetime.now()
total =Etime-Stime
print "Port Scanning Completed in " , total
