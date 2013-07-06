"""
Urls for porticus
"""
from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('porticus.views',
    url(r'^$', 'view_gallery_list', name='porticus-gallery-list'),
    url(r'^page/(?P<page>\d+)/$', 'view_gallery_list', name='porticus-gallery-list-paginated'),
    url(r'^(?P<slug>[-\w]+)/$', 'view_gallery_detail', name='porticus-gallery-detail'),
    url(r'^(?P<slug>[-\w]+)/page/(?P<page>\d+)/$', 'view_gallery_detail', name='porticus-gallery-detail-paginated'),
)
