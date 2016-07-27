##############################################################
# A Multi-Thread TCP Scanning Program to Detect Live System  #
##############################################################
import threading
import time
import socket, subprocess,sys
import thread
import collections
from datetime import datetime
#Initialize Network Address for Ping Sweeping
netaddress = raw_input("Enter the Network Address ")
startNum = int(raw_input("Enter the Starting Number "))
endNum = int(raw_input("Enter the Last Number "))
endNum=endNum+1
dic = collections.OrderedDict()
netlist= netaddress.split('.')
dot = '.'
netspace = netlist[0]+dot+netlist[1]+dot+netlist[2]+dot

#Record Ping Sweeping Start Time
Stime= datetime.now()

class myThread (threading.Thread):
    def __init__(self,startNum,endNum):
        threading.Thread.__init__(self)
        self.startNum = startNum
        self.endNum = endNum
    def run(self):
        Running(self.startNum,self.endNum)

def Scanning (address):
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((address,80))
    if result == 0:
        sock.close()
        return 1
    else :
        sock.close()

def Running (startNum,endNum):
    for ip in xrange(startNum,endNum):
        address = netspace+str(ip)
        if (Scanning(address)):
            dic[ip] = address

#Define Total Thread to Be Run
total_ip =endNum-startNum
num =20 # number of ip handled by one thread
total_thread = total_ip/num
total_thread=total_thread+1
threads= []

#Start Ping Sweep with Threads
try:
    for i in xrange(total_thread):
        ending = startNum+num
        if(ending > endNum):
            ending = endNum
        thread = myThread(startNum,ending)
        thread.start()
        threads.append(thread)
        startNum = ending
except Exception as e:
    print ("Error: unable to start thread is %s" % (e))
print "\tNumber of Threads active:", threading.activeCount()

for t in threads:
    t.join()
print "Exiting Main Thread"
dictionary = collections.OrderedDict(sorted(dic.items()))
for key in dictionary:
    print dictionary[key],"--> Live"

#Record Ping Sweeping End Time
Etime= datetime.now()
#Calculate Total Time for Ping Sweeping
total =Etime-Stime
print "TCP Sweeping Completed in " , total
