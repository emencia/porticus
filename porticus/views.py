"""
Views for porticus
"""
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.exceptions import ImproperlyConfigured

from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.list import BaseListView

from porticus.models import Gallery, Album, Ressource


class SimpleListView(TemplateResponseMixin, BaseListView):
    """
    Like generic.ListView but use only ``get_template`` to find template and not an
    automatic process on ``get_template_names``
    """
    pass


class DetailListView(SimpleListView):
    """
    Like SimpleListView but require a detail object model that will be used to 
    find a list object from his relations
    """
    detail_model = None
    detail_slug = None
    context_parent_object_name = 'detail_object'

    def get_detail_slug(self):
        return self.detail_slug or self.kwargs.get('detail_slug')

    def get_detail_object(self):
        if self.detail_model is None:
            raise ImproperlyConfigured(u"%(cls)s's 'detail_model' class attribute must be defined " % {"cls": self.__class__.__name__})
        return get_object_or_404(self.detail_model, slug=self.get_detail_slug(), publish=True)

    def get(self, request, *args, **kwargs):
        self.detail_object = self.get_detail_object()
        return super(DetailListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs.update({
            self.context_parent_object_name: self.detail_object,
        })
        return super(DetailListView, self).get_context_data(**kwargs)


class GalleryListView(SimpleListView):
    """
    View to diplay a paginated list of galleries
    """
    paginate_by = settings.PORTICUS_GALLERIES_PAGINATION
    model = Gallery
    template_name = "porticus/gallery_list.html"


class GalleryDetailView(DetailListView):
    detail_model = Gallery
    context_parent_object_name = 'gallery_object'
    
    model = Album
    paginate_by = settings.PORTICUS_ALBUMS_PAGINATION

    def get_queryset(self):
        return self.detail_object.album_set.filter(publish=True).order_by('priority', 'name')
    
    def get_template_names(self):
        return (self.detail_object.template_name,)


class GalleryTreeView(GalleryDetailView):
    """
    Display the album tree for a gallery, inherit from GalleryDetailView, does not 
    follow the gallery template
    """
    paginate_by = None
    template_name = "porticus/gallery_tree.html"

    def get_queryset(self):
        return self.detail_object.album_set.filter(publish=True)
    
    def get_template_names(self):
        return (self.template_name,)


class AlbumDetailView(DetailListView):
    detail_model = Album
    parent_slug = None
    context_parent_object_name = 'album_object'
    
    model = Ressource
    paginate_by = settings.PORTICUS_RESSOURCES_PAGINATION

    def get_parent_slug(self):
        return self.parent_slug or self.kwargs.get('parent_slug')

    def get_detail_object(self):
        self.gallery_object = get_object_or_404(Gallery, slug=self.get_parent_slug(), publish=True)
        return super(AlbumDetailView, self).get_detail_object()

    def get_queryset(self):
        return self.detail_object.get_published_ressources()

    def get_context_data(self, **kwargs):
        kwargs.update({
            'gallery_object': self.gallery_object,
        })
        return super(AlbumDetailView, self).get_context_data(**kwargs)
    
    def get_template_names(self):
        return (self.detail_object.template_name,)
