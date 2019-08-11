#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/11 1:50 PM

# urls.py
from django.conf.urls.defaults import  *

urlpatterns = patterns('blog.views', 
    (r'^$', 'archive'),
    (r'^create/', 'create_blogpost')
)