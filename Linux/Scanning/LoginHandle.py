##############################################################
#             Handling Data in Login Page Database           #
##############################################################
import shelve
def create():
    print "Login Page Database Will be Created...."
    s = shelve.open("login.dat",writeback=True)
    s['php']= []

def update():
    s = shelve.open("login.dat",writeback=True)
    num = int(raw_input("Enter the Number of Login Page: "))
		
    for x in range(num):
        val = raw_input("Enter the Login Page: ")
        (s['php']).append(val)
    s.sync()
    s.close()

def retrieve():
    s = shelve.open("login.dat",writeback=True)
    for key in s:
        print "*"*40
        print key
        print s[key]
        print "Total Number ", len(s['php'])
    s.close()

while (True):
    print "Press"
    print "C for Create"
    print "U for Update"
    print "R for Retrieve"
    print "E for exit"
    print "*"*40
    c=raw_input("Enter: ")  
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
