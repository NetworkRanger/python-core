#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/10 12:18 PM

import os
import re

f = os.popen('who', 'r')
for eachLine in f:
    print(re.split(r'\s\s+|\t', eachLine.rstrip()))
f.close()