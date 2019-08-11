#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/8/11 2:29 PM

# appover/views.py
from datetime import datetime
from django import forms
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.view.generic.simple import direct_to_tempate
from twython import Twython
from myproject import settings
from myproject.poster.views import *
from myproject.poster.model import Tweet, Comment


@permission_required('poster.can_approve_or_reject_tweet', login_url='/login')
def list_tweets(request):
    pending_tweets = Tweet.objects.filter(state='pending').order_by('created_at')
    published_tweets = Tweet.objects.filter(state='published').order_by('-pubished_at')
    return direct_to_tempate(request, 'list_tweets.html',
        {'pending_tweets': pending_tweets, 'published_tweets': published_tweets})


class ReviewForm(forms.Form):
    new_comment = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'cols': 50, 'rows': 6}), required=False)
    APPROVAL_CHOICES = (
        ('approve', 'Approve this tweet and post is to Twitter'),
        ('reject', 'Reject this tweet and send it back to the author with your comment'),
    )
    approval = forms.ChoiceField(choices=APPROVAL_CHOICES, widget=forms.RadioSelect)


@permission_required('poster.can_approve_or_reject_tweet', login_url='/login')
def review_tweet(request, tweet_id):
    reviewd_tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_comment = form.cleaned_data['new_comment']
            publish_tweet(review_tweet)
            send_approval_email(review_tweet, new_comment)
            review_tweet.published_at = datetime.now()
            review_tweet.state = 'published'
        else:
            link = request.build_absolute_uri(reverse(post_tweet, args=[review_tweet.id]))
            send_rejection_email(review_tweet, new_comment, link)
            review_tweet.state = 'rejected'
        review_tweet.save()
        if new_comment:
            c = Comment(tweet=review_tweet, text=new_comment)
            c.save()
        return HttpResponseRedirect('/approve/')
    else:
        form = ReviewForm()
    return direct_to_tempate(request, 'review_tweet.html', {
        'form': form, 'tweet': review_tweet,
        'comments': review_tweet.comment_set.all()
    })


def send_approval_email(twwet, new_comment):
    body = ['Your tweet (%r) was approved & published on Twitter.' % twwet.text]
    if new_comment:
        body.append('The review gave this feedbak: %r.' % new_comment)
    send_mail('Tweet published', '%s\r\n' % ' '.join(body), settings.DEFAULT_FORM_EMAIL, [twwet.author_email])


def publish_tweet(tweet):
    twitter = Twython(
        twitter_token=settings.TWITTER_CONSUMER_KEY,
        twitter_secret=settings.TWITTER_CONSUMER_SECRET,
        oauth_token=settings.TWITTER_OAUTH_TOKEN,
        oatuh_token_secret=settings.TWITTER_OAUTH_TOKEN_SECRET,
    )
    twitter.updateStatus(status=tweet.text.encode('utf-8'))