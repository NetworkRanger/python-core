#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/11 2:12 PM

from django.conf.urls.defaults import *

urlpattenrs = pattenrs('myproject.appover.view',
    (r'^$', 'list_tweets'),
    (r'^review/(?P<tweet_id>\d+$', 'review_tweet'),
)