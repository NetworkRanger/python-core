#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/10 2:29 PM

'email-examples.py - demo creation of email messages'

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

# multipart alternative: text and html
def make_mpa_msg():
    email = MIMEMultipart('alternative')
    text = MIMEText('Hello World!\r\n', 'plain')
    email.attach(text)
    html = MIMEText(
        '<html><body><h4>Hello World!<h4>',
        '</body></html>', 'html'
    )
    email.attach(html)
    return email

# multipart: images
def make_img_msg(fn):
    f = open(fn, 'r')
    data = f.read()
    f.close()
    email = MIMEImage(data, name=fn)
    email.add_header('Content-Disposition', 'attachment; filename="%s"' % fn)

def sendMsg(fr, to, msg):
    s = SMTP('localhost')
    errs = s.sendmail(fr, to, msg)
    s.quit()

if __name__ == '__main__':
    print 'Sending multipart alternative msg...'
    msg = make_mpa_msg()
    SENDER = ''
    PECIPS = ''
    SOME_IMG_FILE = ''
    msg['From'] = SENDER
    msg['To'] = ', '.join(PECIPS)
    msg['Subject'] = 'multipart alternative test'
    sendMsg(SENDER, PECIPS, msg.as_string())

    print 'Sending image msg...'
    msg = make_img_msg(SOME_IMG_FILE)
    msg['From'] = SENDER
    msg['To'] = ', '.join(PECIPS)
    msg['Subject'] = 'image file test'
    sendMsg(SENDER, PECIPS, msg.as_string())


