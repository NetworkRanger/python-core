#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/11 12:38 PM

import cgi
from urllib import quote_plus

header = 'Content-Type: text/html\n\n'
url = '/cgi-bin/friendsC.py'

errhtml = '''
<html>
<head>
<title>Friends CGI Demo</title>
</head>
<body>
<h3>ERROR</h3>
<b>%s</b>
<p>
<form>
<input type="button" value="Back" onclick="window.history.back()">
</form>
</body>
</html>
'''

def showError(error_str):
    print header + errhtml % error_str

formhtml = '''
<html>
<head>
<title>Friends CGI Demo</title>
</head>
<body>
<h3>Friends list for: <i>%s</i></h3>
<form action="%s">
<b>Enter your Name:</b>
<input type="hidden" name="action" value="edit">
<input type="text" name="person" value="%s" size=15">
<p>
<b>How many friends do you have?</b>%s
</p>
<input type="submit">
</form>
</body>
</html>
'''

fradio = '<input type="radio" name="howmany" value="%s" %s> %s\n'

def showForm(who, howmay):
    friends = []
    for i in (0, 10, 25, 50 ,100):
        checked = ''
        if str(i) == howmay:
            checked = 'CHECKED'
        friends.append(fradio % str(i), checked, str(i))
        print '%s%s' % (header, formhtml % (who, url, who, ''.join(friends)))

reshtml = '''
<html>
<head>
<title>Friends CGI Demo</title>
</head>
<body>
<h3>Friends list for: <i>%s><i><h3>
Your name is: <b>%s<b>
<p>
Click <a href="%s">here</a> to edit your data again.
</p>
</body>
</html>
'''

def doResults(who, howmany):
    newurl = url + '?action=reedit&person=%s&howmay=%s' % (quote_plus(who), howmany)
    print header + reshtml % (who, who, howmany, newurl)

def process():
    error = ''
    form = cgi.FieldStorage()

    if 'person' in form:
        who = form['person'].value.title()
    else:
        who = 'NEW USER'

    if 'howmany' in form:
        howmany = form['howmay'].value
    else:
        if 'aciton' in form and form['action'].value != 'reedit':
            error = 'Please select number of friends.'
        else:
            howmany = 0

    if not error:
        if 'action' in form and form['action'].value != 'reedit':
            doResults(who, howmany)
        else:
            showForm(who, howmany)
    else:
        showError(error)

if __name__ == '__main__':
    process()
