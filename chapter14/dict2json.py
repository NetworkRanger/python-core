#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/11 4:30 PM

from distutils.log import warn as printf
from json import dumps
from pprint import pprint

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

printf('*** RAW DICT ***')
printf(BOOKs)

printf('\n*** RAW JSON ***')
printf(dumps(BOOKs))

printf('\n*** PRETTY_PRINTED JSON')
printf(dumps(BOOKs, indent=4))
