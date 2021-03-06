###########################################################################
#        A Ping Sweeping Program with Thread to Detect Live System        #
###########################################################################
import os
import collections
import platform
import socket, subprocess,sys
import threading
from datetime import datetime
#Initialize Network Address for Ping Sweeping
netaddress = raw_input("Enter the Network Address ")
netlist= netaddress.split('.')
dot = '.'
netspace = netlist[0]+dot+netlist[1]+dot+netlist[2]+dot
startNum = int(raw_input("Enter the Starting Number "))
endNum = int(raw_input("Enter the Last Number "))
endNum=endNum+1

#Define A Ordered Dictionary to Store IP Address
dic = collections.OrderedDict()

#Identity the Local Platform for Ping Sweeping
operating = platform.system()

#Identify Ping Command for Ping Sweeping Based on Platform
if (operating=="Windows"):
    Cping = "ping -n 1 "
elif (operating== "Linux"):
    Cping = "ping -c 1 "
else :
    Cping = "ping -c 1 "

#Record Ping Sweeping Start Time
Stime= datetime.now()

class myThread (threading.Thread):
    def __init__(self,startNum,endNum):
        threading.Thread.__init__(self)
        self.startNum = startNum
        self.endNum = endNum
    def run(self):
        Running(self.startNum,self.endNum)

def Running (startNum,endNum):
    #Conduct Ping Sweeping
    print "Scanning in Progress"
    for ip in xrange(startNum,endNum):
        address = netspace+str(ip)
        command = Cping+address
        response = os.popen(command)
        for line in response.readlines():
            if (line.count("ttl")):
                break
        if (line.count("ttl")):
            #print address, "--> Live"
            dic[ip]= address

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
print "Ping Sweeping Completed in " , total
