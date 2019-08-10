#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/10 10:29 PM

from distutils import setup, extension

MOD = 'Extest'
setup(name=MOD, ext_modules=[extension(MOD, sources=['Extest2.c'])])