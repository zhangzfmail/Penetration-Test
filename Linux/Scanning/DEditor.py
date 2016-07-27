##############################################################
#          Shelve Database Editor for Port Scanning          #
##############################################################
import shelve

def create():
    shelf = shelve.open("port.dat", writeback=True)
    shelf['desc'] ={}
    shelf.close()
    print "Dictionary is Created"

def update():
    shelf = shelve.open("port.dat", writeback=True)
    data=(shelf['desc'])
    port =int(raw_input("Enter the Port: "))
    data[port]= raw_input("Enter the description: ")
    shelf.close()

def deletekey():
    shelf = shelve.open("port.dat", writeback=True)
    data=(shelf['desc'])
    port =int(raw_input("Enter the Port: "))
    del data[port]
    shelf.close()
    print "Entry is deleted"

def listkey():
    print "#"*40
    shelf = shelve.open("port.dat", writeback=True)
    data=(shelf['desc'])
    for key, value in data.items():
        print key, ":", value
    print "#"*40

print "Port Scanning Database Editor"
while(True):
    print "Please Input Command for Editting Database" 
    print "C for Creating a Database"
    print "U for Updating or Adding a Record"
    print "D for Deleting a Record"
    print "L for Listing All Records"
    print "E for Exiting"
    c=raw_input("Enter :  ")  

    if (c=='C' or c=='c'):
        create()
    elif (c=='U' or c=='u'):
        update()
    elif(c=='D' or c=='d'):
        deletekey()
    elif(c=='L' or c=='l'):
        listkey()	
    elif(c=='E' or c=='e'):
        exit()
    else:
        print "Incorrect Input"
