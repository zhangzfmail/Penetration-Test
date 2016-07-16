##################################################################################################
#                      A Ping Sweeping Program to Detect Live System                             #
##################################################################################################
import os
import platform
from datetime import datetime
#Initialize Network Address for Ping Sweeping
netaddress = raw_input("Enter the Network Address ")
netlist= netaddress.split('.')
dot = '.'
netspace = netlist[0]+dot+netlist[1]+dot+netlist[2]+dot
start = int(raw_input("Enter the Starting Number "))
end = int(raw_input("Enter the Last Number "))
end=end+1

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

#Conduct Ping Sweeping
print "Scanning in Progress"
for ip in xrange(start,end):
    address = netspace+str(ip)
    command = Cping+address
    response = os.popen(command)
    for line in response.readlines():
        if (line.count("TTL")):
            print address, "--> Live"
        if (line.count("ttl")):
            print address, "--> Live"

#Record Ping Sweeping End Time
Etime= datetime.now()

#Calculate Total Time for Ping Sweeping
total =Etime-Stime
print "Ping Sweeping Completed in " , total
