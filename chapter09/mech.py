#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/11 9:39 AM

from BeautifulSoup import BeautifulSoup, SoupStrainer
from mechanize import Browser

BS = lambda page: page
YOUR_LOGIN = ''
YOUR_PASSWD = ''

br = Browser()

# home page
rsp = br.open('http://us.pycon.org/2011/home/')
print '\n***', rsp.geturl()
print "Confirm home page has 'Login in' link; click it"
page = rsp.read()
assert 'Log in' in page, 'Log in not in page'
rsp = br.follow_link(text_regex='Log in')

# login page
print '\n***', rsp.geturl()
print 'Error due to invalid creds; resubmit w/valid creds'
assert rsp.geturl() == 'http://us.pycon.org/2011/account/login/', rsp.geturl()

page = rsp.read()
err = str(BS(page).find('div', {'id': 'errorMsg'}).find('ul').find('li').string)
assert err  == 'The username and/or password you specified are not correct.', err
br.select_form(nr=0)
br.form['username'] = YOUR_LOGIN
br.form['password'] = YOUR_PASSWD
rsp = br.submit()

# login successful, home page redirect
print '\n***', rsp.geturl()
print 'Logged in properyly on home page; click Account link'
assert rsp.geturl == 'http://us.pycon.org/2011/home/', rsp.geturl()
page = rsp.read()
assert 'Logout' in page, 'Logout not in page'
rsp = br.follow_link(text_regex='Account')

# account page
print '\n**', rsp.geturl()
print 'Email address parseable on Account page; go back'
assert rsp.geturl() == 'http://us.pycon.org/2011/account/email/', rsp.geturl()
page = rsp.read()
assert 'Email Address' in page, 'Missing email address'
print '    Primary e-mail: %r' % str(BS(page).find('table').find('tr').find('td').find('b').string)
rsp = br.back()

# back to home page
print '\n***', rsp.geturl()
print 'Back works, on home page again; click Logout link'
rsp = br.follow_link(url_regex='logout')

# logout page
print '\n***', rsp.geturl()
print 'Confirm on Logout page and Log in link at the top'
assert rsp.geturl() == 'http://us.pycon.org/2011/account/logout/', rsp.geturl()
page = rsp.read()
assert 'Log in' in page, 'Log in not in page'
print '\n*** DONE'

