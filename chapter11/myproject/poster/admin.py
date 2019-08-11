#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/11 2:18 PM

from django.contrib import admin
from models import *

admin.site.register(Tweet, Comment)