#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/11 2:04 PM

# urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = ('',
    # (r'^post/', include('myproject.poster.urls')),
    # (r'^$', include('myproject.poster.urls')),
    # (r'^approve/', include('admin.site.urls')),
    (r'^login', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout', 'djnao.contrib.auth.view.logout'),
)
