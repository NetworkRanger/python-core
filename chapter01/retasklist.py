#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/10 12:22 PM

import os
import re

f = os.popen('tasklist /nh', 'r')
for eachLine in f:
    print(re.findall(r'([\w.]+(?:[\w.]+)*\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K))', eachLine.rstrip()))
f.close()