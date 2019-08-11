#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/11 12:17 PM

import cgi

reshtml = '''Content-Type: text/html\n
<html>
<head>
<title>Friends CGI Demo (dynamic screen)</title>
</head>
<body>
<h3>Friends list for: <i>%s</i></h3>
Your name is: <b>%s</b>
<p>
You have <b>%s</b> friends.
</p>
</body>
</html>
'''

form = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value
print reshtml % (who, who, howmany)