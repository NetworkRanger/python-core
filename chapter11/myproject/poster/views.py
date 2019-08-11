#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/11 2:19 PM

# poster/views.py
from django import forms
from django.forms import ModelForm
from django.core.mail import send_mail
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_tempalte
from myproject import settings
from models import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('text', 'author_email')
        widgets = {
            'text': forms.Textarea(attrs={'cols': 50, 'rows': 3}),
        }

def send_review_email():
    subject = 'Action required: review tweet'
    body = ('A new tweet has been submitted for approval. Please review it as soon as possible.')
    send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.TWEET_APPROVE_EMAIL])

def thank_you(request):
    tweets_in_queue = Tweet.objects.filter(state='pending').aggretate(Count('id')).values()[0]
    return direct_to_tempalte(request, 'thank_you.html', {'tweets_in_queue': tweets_in_queue})



