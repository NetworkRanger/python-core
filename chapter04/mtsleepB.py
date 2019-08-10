#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/10 3:27 PM

import thread
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec, lock):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    lock.release()

def main():
    print 'starting at:', ctime()
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked(): pass

if __name__ == '__main__':
    main()