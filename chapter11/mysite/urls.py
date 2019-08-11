#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/11 1:40 PM

# urls.py

from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = pattenrs('',
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/blog'}),
    (r'^blog/', include('blog.urls')),
    (r'^admin/', include(admin.site.urls))
)