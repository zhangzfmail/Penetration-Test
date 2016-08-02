##############################################################
#           Obtain HTTP Field from Page Source               #
##############################################################
import urllib
from bs4 import BeautifulSoup
url = raw_input("Enter the URL: ")
field = raw_input("Enter the Field from Source Page: ")
attribute = raw_input("Enter the Attribute from the Field: ")
attr_field = raw_input("Enter the Attribute Content: ")
http= urllib.urlopen(url)
html_page = http.read()
BS_object = BeautifulSoup(html_page)
data = BS_object.find(field, id = id_field)
print data
