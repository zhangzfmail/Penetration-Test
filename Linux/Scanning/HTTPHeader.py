##############################################################
#                        HTTP Error Handling                 #
##############################################################
import urllib
url = raw_input("Enter the URL: ")
http_r = urllib.urlopen(url)
if http_r.code == 200:
    print http_r.headers
