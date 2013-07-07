"""
Urls for porticus
"""
from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('porticus.views',
    url(r'^$', 'view_album_list', name='porticus-album-list'),
    url(r'^page/(?P<page>\d+)/$', 'view_album_list', name='porticus-album-list-paginated'),
    url(r'^(?P<slug>[-\w]+)/$', 'view_album_detail', name='porticus-album-detail'),
    url(r'^(?P<slug>[-\w]+)/page/(?P<page>\d+)/$', 'view_album_detail', name='porticus-album-detail-paginated'),
)
