##############################################################
#                        HTTP Error Handling                 #
##############################################################
import re
import random
import urllib
url_origin = raw_input("Enter the URL: ")
seed = chr(random.randint(97,122))
url = url_origin+seed
http_r = urllib.urlopen(url)

content= http_r.read()
#Number to Determine if Loop is Stopped Because a Vulnerable Website is Found
flag =0
#Number to Determine if a Tag is Found
i=0
#Define a List to Store Matching Position in Web Content
Mlist = []
a_tag = '<*address>'
file_text = open("result.txt",'a')

while flag ==0:
    if http_r.code == 404:
        file_text.write("--------------")
        file_text.write(url_origin)
        file_text.write("--------------\n")
        file_text.write(content)
		
        for match in re.finditer(a_tag,content):
            i=i+1
            s= match.start()
            e= match.end()
            Mlist.append(s)
            Mlist.append(e)
        if (i>0):
            print "The Website Error Handling is Vulnerable"
        if len(Mlist)>0:
            a= Mlist[1]
            b= Mlist[2]
            print (content[a:b])[:-2]
        else:
            print "The Website Error Handling is not Vulnerable"
        flag =1
    elif http_r.code == 200:
        print "The Website Error Handling Page is Customized"
        break
