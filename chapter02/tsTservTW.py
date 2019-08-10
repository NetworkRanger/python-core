#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/10 1:31 PM

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServerProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print '...connected from:', clnt

    def dataReceived(self, data):
        self.transport.write('[%s] %s' % (ctime(), data))

factory = protocol.Factory()
factory.protocol = TSServerProtocol
print 'waiting for connection...'
reactor.listenTCP(PORT, factory)
reactor.run()