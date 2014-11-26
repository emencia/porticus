"""
Urls for porticus
"""
from django.conf.urls import url, patterns
from porticus.views import GalleryListView, GalleryDetailView, GalleryTreeView, AlbumDetailView, AlbumTagRessourcesView, RessourceDetailView

urlpatterns = patterns('porticus.views',
    url(r'^$', GalleryListView.as_view(), name='galleries-index'),
    
    url(r'^(?P<gallery_slug>[-\w]+)/$', GalleryDetailView.as_view(), name='gallery-detail'),
    url(r'^tree/(?P<gallery_slug>[-\w]+)/$', GalleryTreeView.as_view(), name='gallery-tree'),
    
    url(r'^(?P<gallery_slug>[-\w]+)/(?P<album_slug>[-\w]+)/$', AlbumDetailView.as_view(), name='album-detail'),
    url(r'^(?P<gallery_slug>[-\w]+)/(?P<album_slug>[-\w]+)/(?P<ressource_slug>[-\w]+)/$', RessourceDetailView.as_view(), name='ressource-detail'),
    url(r'^(?P<gallery_slug>[-\w]+)/(?P<album_slug>[-\w]+)/tag/(?P<tag>[-\w\ ]+)/$', AlbumTagRessourcesView.as_view(), name='album-tag'),
)
