##############################################################
#         Whois Information from Designated Domain           #
##############################################################
import urllib
from bs4 import BeautifulSoup
import re
domain=raw_input("Enter the Domain Name: ")
url = "http://www.whois.com/whois/"+str(domain)
http= urllib.urlopen(url)
html_page = http.read()
BS_object = BeautifulSoup(html_page)
file_text= open("who.txt",'a')
who_is_raw = BS_object.body.find('div',attrs={'class' : 'whois_result'})
who_is = str(who_is_raw)

for match in re.finditer("Domain Name:",who_is):
    s= match.start()

lines_raw = who_is[s:]
lines = lines_raw.split("<br/>",100)
i=0
for line in lines[:-1] :
    file_text.writelines(line)
    file_text.writelines("\n")
    print line
    i=i+1
    if i==17 :
        break
file_text.writelines("-"*50)
file_text.writelines("\n")
file_text.close()
