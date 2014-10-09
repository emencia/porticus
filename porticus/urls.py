"""
Urls for porticus
"""
from django.conf.urls.defaults import url, patterns
from porticus.views import GalleryListView, GalleryDetailView, GalleryTreeView, AlbumDetailView, AlbumTagDetailView

urlpatterns = patterns('porticus.views',
    url(r'^$', GalleryListView.as_view(), name='porticus-galleries-index'),
    
    url(r'^(?P<gallery_slug>[-\w]+)/$', GalleryDetailView.as_view(), name='porticus-gallery-detail'),
    url(r'^tree/(?P<gallery_slug>[-\w]+)/$', GalleryTreeView.as_view(), name='porticus-gallery-tree'),
    
    url(r'^(?P<gallery_slug>[-\w]+)/(?P<album_slug>[-\w]+)/$', AlbumDetailView.as_view(), name='porticus-album-detail'),
    url(r'^(?P<gallery_slug>[-\w]+)/(?P<album_slug>[-\w]+)/tag/(?P<tag>[-\w\ ]+)/$', AlbumTagDetailView.as_view(), name='porticus-album-tag'),
)
