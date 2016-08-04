##############################################################
#                        Handle XSS Database                 #
##############################################################
import shelve
def create():
    print "XSS Database is Created...."
    s = shelve.open("xss.dat",writeback=True)
    s['xss']= []

def update():
    s = shelve.open("xss.dat",writeback=True)
    number = int(raw_input("Enter the Number of Values: "))
		
    for x in range(number):
        val = raw_input("Enter the XSS Value: ")
        (s['xss']).append(val)
    s.sync()
    s.close()

def retrieve():
    s = shelve.open("xss.dat",writeback=True)
    for key in s:
        print "*"*40
        print key
        print s[key]
        print "Total Number: ", len(s['xss'])
    s.close()

while (True):
    print "Press"
    print "C for Create"
    print "U for Update"
    print "R for retrieve"
    print "E for exit"
    print "*"*40
    c=raw_input("Please Enter: ")  
    if (c=='C' or c=='c'):
        create()
    elif(c=='U' or c=='u'):
        update()
    elif(c=='R' or c=='r'):
        retrieve()
    elif(c=='E' or c=='e'):
        exit()
    else:
        print "\t Wrong Input"
