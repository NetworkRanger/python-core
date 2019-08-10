#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/10 4:32 PM

from concurrent.futures import ThreadPoolExecutor
from re import compile
from time import ctime
from urllib2 import urlopen as uopen

REGEX = compile('#([\d,]+) in Books')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}

def getRanking(isbn):
    with uopen('{0}{1}'.format(AMZN, isbn)) as page:
        return str(REGEX.findall(page.read())[0], 'utf-8')

def main():
    print 'At', ctime(), 'on Amazon...'
    with ThreadPoolExecutor(3) as executor:
        for isbn, ranking in zip(ISBNs, executor.map(getRanking, ISBNs)):
            print '- %r ranked %s' % (ISBNs[isbn], ranking)
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()