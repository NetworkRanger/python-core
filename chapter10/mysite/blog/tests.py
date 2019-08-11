#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/11 1:43 PM

# tests.py

from datetime import datetime
from django.test import TestCase
from django.test import Client
from blog.models import BlogPost

class BlogPostTest(TestCase):
    def test_obj_create(self):
        BlogPost.objects.create(title='raw title', body='raw body', timestamp=datetime.now())
        self.assertEqual(1, BlogPost.objects.count())
        self.assertEqual('raw title', BlogPost.objects.get(id=1).title)

    def test_home(self):
        response = self.client.get('/blog/')
        self.failUnlessEqual(response.status_code, 200)

    def test_slash(self):
        response = self.client.get('/')
        self.assertIn(response.status_code, (301, 302))

    def test_empty_create(self):
        response = self.client.get('/blog/create/')
        self.assertIn(response.status_code, (301, 302))
        self.assertEqual(1, BlogPost.objects.count())
        self.assertEqual('post title', BlogPost.objects.get(id=1).title)

