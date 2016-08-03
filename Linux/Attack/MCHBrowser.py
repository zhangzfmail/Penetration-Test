##############################################################
#                       Mechanize Browser                    #
##############################################################
import mechanize
br = mechanize.Browser()
br.set_handle_robots( False )
url = raw_input("Enter URL ")
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

for i in range(5):
    br.open(url)
    for form in br.forms():
        #print form
        num = 0
        br.select_form(nr=num)
        br.form['name'] = 'User2'
        br.form['comment'] = ''
        br.submit()
        num = num + 1
