#!/usr/local/bin/python
##############################################################################
# 'getfeed.py'

import cPickle
import feedparser

item_stub = {
    "title": None,
    "link": None,
    "pubDate": None,
    "comments": None,
    "guid": None,
    }

def get_feed(feedurl):
    feed_data = feedparser.parse(feedurl)
    feed_data['entries'].reverse()

    return feed_data

