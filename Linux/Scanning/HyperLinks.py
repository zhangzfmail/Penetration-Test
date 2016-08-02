##############################################################
#                        HTTP Error Handling                 #
##############################################################
import urllib
from bs4 import BeautifulSoup
url = raw_input("Enter the URL: ")
ht= urllib.urlopen(url)
html_page = ht.read()
BS_object = BeautifulSoup(html_page)
print BS_object.title.text
for link in BS_object.find_all('a'):
    print(link.get('href'))
