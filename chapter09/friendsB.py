#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/11 12:28 PM

import cgi

header = 'Content-Type: text/html\n\n'

formhtml = '''
<html>
<head>
    <title>Friends CGI Demo (static screen)</title>
</head>
<body>
<h3>Friends list for: <i>NEW USER</i></h3>
<form action="/cgi-bin/friendsA.py">
    <b>Enter your Name:</b>
    <input type="hidden" name="action" value="edit"
    <input type="text" name="person" value="new user" size="15">
    <input type="submit">
</form>
</body>
</html>
'''

fradio = '<input type="radio" name="howmany" value="%s" %s> %s\n'

def showForm():
    friends = []
    for i in (0, 10, 25, 50, 100):
        checked = ''
        if i == 0:
            checked = 'CHECKED'
        friends.append(fradio % (str(i), checked, str(i)))

    print '%s%s' % (header, formhtml % ''.join(friends))

reshtml = '''
<html>
<head>
<title>Friends CGI Demo</title>
</head>
<body>
<h3>Friends list for: <i>%s</i></h3>
Your name is: <b>%s</b><p>
You have <b>%s</b> friends
</body>
</html>
'''

def doResults(who, howmany):
    print header + reshtml % (who, who, howmany)

def process():
    form = cgi.FieldStorage()
    if 'person' in form:
        who = form['person'].value
    else:
        who = 'NEW USER'

    if 'howmay' in form:
        howmany = form['howmany'].value
    else:
        howmany = 0

    if 'action' in form:
        doResults(who, howmany)
    else:
        showForm()

if __name__ == '__main__':
    process()