##############################################################
#                Search Login Page for PHP Website           #
##############################################################
import httplib
import shelve
url = raw_input("Enter the full URL: ")

def handleURL (url):
    temp_url = url.replace("http://","")
    url_split = temp_url.split('/')
    target = url_split[0]
    if (url_split[-1] == ''):
        site = temp_url[:-1]
    else:
        site = temp_url
    return target, site

target, site = handleURL(url)

pages = shelve.open("login.dat",writeback=True)

for page in pages['php']:
    delimiter = "/"
    url_login = site+delimiter+page
    print '#'*40
    print url_login
    http_r = httplib.HTTPConnection(target)
    page = url_login.replace(target,"")
    print page
    print '#'*40
    http_r.request("GET",page)
    reply = http_r.getresponse()
	
    if reply.status == 200:
        print "URL found ----> ", url_login
        ch = raw_input("Press [C/c] for Continue: ")
        if ch == "C" or ch == "c" : 
            continue 
        else :
            break
	
pages.close()
