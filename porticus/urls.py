"""Urls for porticus"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns(
    'porticus.views',
    url(r'^$',
        'view_gallery_list',
        name='gallery_gallery_list'),
    url(r'^page/(?P<page>\d+)/$',
        'view_gallery_list',
        name='gallery_gallery_list_paginated'),
    url(r'^(?P<slug>[-\w]+)/$',
        'view_gallery_detail',
        name='gallery_gallery_detail'),
    url(r'^(?P<slug>[-\w]+)/page/(?P<page>\d+)/$',
        'view_gallery_detail',
        name='gallery_gallery_detail_paginated'),
    )
