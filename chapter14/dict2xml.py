#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/11 4:34 PM

from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

BOOKs = {
    '0132269937': {
        'title': 'Corn Python Programming',
        'edition': 2,
        'year': 2007,
    },
    '0132356139': {
        'title': 'Python Web Development with Django',
        'authors': ['Jeff Forcier', 'Paul Bissex', 'Wesley Chun'],
        'year': 2009,
    },
    '0137143419': {
        'title': 'Python Fundamentals',
        'year': 2009,
    }
}

books = Element('books')
for isbn, info in BOOKs.iteritems():
    book = SubElement(books, 'book')
    info.setdefault('authors', 'Wesley Chun')
    info.setdefault('edition', 1)
    for key,val in info.iteritems():
        SubElement(book, key).text = ', '.join(str(val).split(':'))

xml = tostring(books)
print '*** RAW XML ***'
print xml

print '\n*** PRETTY-PRETEND XML ***'
dom = parseString(xml)
print dom.toprettyxml('    ')

print '*** FLAT STRUNTURE ****'
for elmt in books.getiterator():
    print elmt.tag, '-', elmt.text

print '\n*** TITLES ONLY ***'
for book in books.findall('.//title'):
    print book.text