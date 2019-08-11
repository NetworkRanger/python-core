#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/11 2:10 PM

from django.conf.urls.defaults import *

urlpatterns = patterns('myproject.poster.views',
    (r'^$', 'post_tweet'),
    (r'^thankyou', 'thank_you'),
    (r'^edit/(?P<tweet_id>\d+)', 'post_tweet'),
)
