#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/10 2:52 PM

'gmail.py - demo Gmail SMTP/TLS, SMTP/SSL, POP, IMAP'

from cStringIO import StringIO
from imaplib import IMAP4_SSL
from platform import python_version
from poplib import POP3_SSL
from smtplib import SMTP

# SMTP_SSL added in 2.6
release = python_version()
if release > '2.6.2':
    from smtplib import SMTP_SSL  # fixed in 2.6.3
else:
    SMTP_SSL = None

from secret import *  # you provide MAILBOX, PASSWD

MAILBOX = ''
PASSWD = ''

who = '%s@gmail.com' % MAILBOX
from_ = who
to = [who]

headers = [
    'From: %s' % from_,
    'To: %s' % ', '.join(to),
    'Subject: test SMTP send via 587/TLS',
]
body = [
    'Hello',
    'World!',
]

msg = '\r\n\r\n'.join(('\r\n'.join(headers), '\r\n'.join(body)))

def getSubject(msg, default='(no Subject line)'):
    '''
    getSubject(msg) - iterate over 'msg' looking for
    Subject line; return if found otherwise 'default'
    :param msg:
    :param default:
    :return:
    '''
    for line in msg:
        if line.startswith('Subject:'):
            return line.rstrip()
        if not line:
            return default

# SMTP/TLS
print '*** Doing SMTP send via TLS...'
s = SMTP('smtp.gmail.com', 587)
if release < '2.6':
    s.ehlo() # required in older releases
s.starttls()
if release < '2.5':
    s.ehlo() # required in older releases
s.login(MAILBOX, PASSWD)
s.sendmail(from_, to, msg)
s.quit()
print '   TLS mail sent!'

# POP
print '*** Doing POP recv...'
s = POP3_SSL('pop.gmail.com', 995)
s.user(MAILBOX)
s.pass_(PASSWD)
rv, msg, sz = s.retr(s.stat()[0])
s.quit()
line = getSubject(msg)
print '    Received msg via POP: %r' % line

body = body.replace('587/TLS', '465/SSL')

# SMTP/SSL
if SMTP_SSL:
    print '*** Doing SMTP send via SSL...'
    s = SMTP_SSL('smtp.gmail.com', 465)
    s.sendmail(from_, to, msg)
    s.quit()
    print '    SSL mail sent!'

# IMAP
print '*** Doing IMAP recv...'
s = IMAP4_SSL('imap.gmail.com', 993)
s.login(MAILBOX, PASSWD)
rsp, msgs = s.select('INBOX', True)
rsp, data = s.fetch(msgs[0], '(RFC822)')
line = getSubject(StringIO(data[0][1]))
s.close()
s.logout()
print '   Received msg via IMAP: %r' % line

