##############################################################
# A Multi-Thread Port Scanning Program to Detect Live System #
##############################################################
import threading
import time
import socket, subprocess,sys
from datetime import datetime
import thread
import shelve

#Input Port Description
subprocess.call('clear',shell=True)
shelf = shelve.open("port.dat")
data=(shelf['desc'])

class myThread (threading.Thread):
    def __init__(self, threadName,ip,Sport,Eport,c):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.ip = ip
        self.Sport = Sport
        self.Eport = Eport
        self.c =c
    def run(self):
        scantcp(self.threadName,self.ip,self.Sport,self.Eport,self.c)

def scantcp(threadName,ip,Sport,Eport,c):
    try:
        for port in range(Sport,Eport):
            sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socket.setdefaulttimeout(c)
            result = sock.connect_ex((ip,port))
            if result == 0:
                print "Port Open:---->\t", port,"--", data.get(port, "Not in Database")
            sock.close()

    except KeyboardInterrupt:
         print "You stop this "
         sys.exit()

    except socket.gaierror:
         print "Hostname could not be resolved"
         sys.exit()

    except socket.error:
         print "could not connect to server"
         sys.exit()

    shelf.close()

#Multi-Thread Port Scanning Start
print "#"*40
print "\nMulti-Thread Port Scanning Start\n"

#Input Domain Name or IP Address for Scanning
while (True):
    name=raw_input("Press D for Domain Name or Press I for IP Address: ")
    if (name=='D' or name=='d'):
        domain = raw_input("Enter the Domain Name to Scan: ")
        ip = socket.gethostbyname(domain)
        break
    elif(name=='I' or name=='i'):
        ip = raw_input("Enter the IP Address to Scan: ")
        break
    else:
        print "Incorrect Input"

Sport = int(raw_input("Enter the Starting Port Number: "))
Eport = int(raw_input("Enter the Ending Port Number: "))

while (True):
    connect=raw_input("Press L for Low Connectivity and Press H for High connectivity: ")
    if (connect=='L' or connect=='l'):
        c =1.5
        break
    elif(connect =='H' or connect=='h'):
        c=0.5
        break
    else:
        print "Incorrect Input"

print "Multi-Thread Port Scanning is Running on ",ip
print "\n"
print "#"*40

Stime= datetime.now()
tcpport=Eport-Sport

#Number of Port Handled by One Thread
number =30
#Number of Threads
tnum=tcpport/number
if (tcpport%number != 0):
    tnum= tnum+1

if (tnum > 300):
    number = tcpport/300
    number= number+1
    tnum=tcpport/number
    if (tcpport%number != 0):
        tnum= tnum+1

threads= []

try:
    for i in range(tnum):
        #TEport Stand for Temporary Ending Port
        TEport=Sport+number
        thread = myThread("T1",ip,Sport,TEport,c)
        thread.start()
        threads.append(thread)
        Sport=TEport
except:
    print "Error: unable to start thread"

print "Number of Threads active:", threading.activeCount()

for t in threads:
    t.join()
print "Exiting Main Thread"
Etime= datetime.now()

total =Etime-Stime
print "Multi-Thread Port Scanning Complete in " , total
