#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/10 2:21 PM

from smtplib import SMTP
from poplib import POP3
from time import ctime, sleep

SMTPSVR = 'smtp.python.is.cool'
POP3SVR = 'pop.python.is.cool'

who = 'wesley@python.is.cool'
origBody = '''\
From:%(who)s
TO: %(who)s
Subject: test msg
Hello World!
''' % {'who': who}

sendSvr = SMTP(SMTPSVR)
errs = sendSvr.sendmail(who, [who], origBody)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10) # wait for mail to be delivered

recvSvr = POP3(POP3SVR)
recvSvr.user('wesley')
recvSvr.pass_('youllNeverGuess')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
# strip headers and compare to orig msg
sep = msg.index('')
recvBody = msg[sep+1:]
assert origBody == recvBody # assert identical