"""
Views for porticus
"""
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.exceptions import ImproperlyConfigured
from django import http

from django.views.generic.list import BaseListView
from django.views.generic.base import TemplateResponseMixin, View, TemplateView

from porticus.models import Gallery, Album, Ressource

from tagging.models import Tag, TaggedItem
from tagging.utils import calculate_cloud


class SimpleListView(TemplateResponseMixin, BaseListView):
    """
    Like generic.ListView but use only ``get_template`` to find template and not an
    automatic process on ``get_template_names``
    """
    pass


class AlbumConfinementMixin(object):
    """
    Mixin that include methods to confine a view that get objects from a specific Gallery+Album

    You still have to load objects yourself with method ``get_gallery_object`` and ``get_album_object``
    in your get/post/whatever view methods.
    """
    gallery_slug = None
    album_slug = None
    ressource_slug = None
    gallery_object = None
    album_object = None
    ressource_object = None

    def get_gallery_slug(self):
        return self.gallery_slug or self.kwargs.get('gallery_slug')

    def get_album_slug(self):
        return self.album_slug or self.kwargs.get('album_slug')

    def get_ressource_slug(self):
        return self.ressource_slug or self.kwargs.get('ressource_slug')

    def get_gallery_object(self):
        return get_object_or_404(Gallery, slug=self.get_gallery_slug(), publish=True)

    def get_album_object(self):
        return get_object_or_404(Album, slug=self.get_album_slug(), publish=True)

    def get_ressource_object(self):
        return get_object_or_404(Ressource, slug=self.get_ressource_slug(), publish=True)

    def get_context_data(self, **kwargs):
        if self.album_object:
            kwargs['album_object'] = self.album_object
        if self.gallery_object:
            kwargs['gallery_object'] = self.gallery_object
        if self.ressource_object:
            kwargs['ressource_object'] = self.ressource_object
        return super(AlbumConfinementMixin, self).get_context_data(**kwargs)


class GalleryListView(SimpleListView):
    """
    View to diplay a paginated list of galleries
    """
    paginate_by = settings.PORTICUS_GALLERIES_PAGINATION
    model = Gallery
    template_name = "porticus/gallery_list.html"


class GalleryDetailView(AlbumConfinementMixin, SimpleListView):
    model = Album
    paginate_by = settings.PORTICUS_ALBUMS_PAGINATION

    def get_queryset(self):
        return self.gallery_object.album_set.filter(publish=True).order_by('priority', 'name')

    def get_template_names(self):
        return (self.gallery_object.template_name,)

    def get(self, request, *args, **kwargs):
        self.gallery_object = self.get_gallery_object()
        return super(GalleryDetailView, self).get(request, *args, **kwargs)


class GalleryTreeView(GalleryDetailView):
    """
    Display the album tree for a gallery, inherit from GalleryDetailView, does not
    follow the gallery template
    """
    paginate_by = None
    template_name = "porticus/gallery_tree.html"

    def get_queryset(self):
        return self.gallery_object.album_set.filter(publish=True)

    def get_template_names(self):
        return (self.template_name,)


class AlbumDetailView(AlbumConfinementMixin, SimpleListView):
    """
    Display the albums ressources and their tags
    """
    model = Ressource
    paginate_by = settings.PORTICUS_RESSOURCES_PAGINATION

    def get_queryset(self):
        return self.album_object.get_published_ressources()

    def get_template_names(self):
        return (self.album_object.template_name,)

    def get_context_data(self, **kwargs):
        kwargs = super(AlbumDetailView, self).get_context_data(**kwargs)

        tags_q = Tag.objects.usage_for_queryset(self.object_list, min_count=1)
        tags_q = calculate_cloud(tags_q, steps=6)

        kwargs.update({
            # Filter ressource tags from the ressource list queryset
            # Behavior to watch, maybe at this step, the queryset has been limited by the paginator
            'ressources_tags': tags_q,
        })
        return kwargs

    def get(self, request, *args, **kwargs):
        self.gallery_object = self.get_gallery_object()
        self.album_object = self.get_album_object()
        return super(AlbumDetailView, self).get(request, *args, **kwargs)

class AlbumTagRessourcesView(AlbumConfinementMixin, SimpleListView):
    """
    Template view to list tagged Ressources from an Album
    """
    model = Ressource
    paginate_by = settings.PORTICUS_RESSOURCES_PAGINATION
    template_name = 'porticus/tag_detail.html'
    tag = None

    def get_tag_object(self):
        tag = self.tag or self.kwargs.get('tag')
        try:
            q = Tag.objects.get(name=tag)
        except Tag.DoesNotExist:
            raise http.Http404
        else:
            return q

    def get_ressources_queryset(self):
        if not hasattr(self, '_get_ressources_queryset_cache'):
            setattr(self, '_get_ressources_queryset_cache', self.album_object.get_published_ressources())
        return getattr(self, '_get_ressources_queryset_cache')

    def get_queryset(self):
        return TaggedItem.objects.get_by_model(self.get_ressources_queryset(), self.tag_object)

    def get_context_data(self, **kwargs):
        kwargs = super(AlbumTagRessourcesView, self).get_context_data(**kwargs)

        tags_q = Tag.objects.usage_for_queryset(self.get_ressources_queryset(), min_count=1)
        tags_q = calculate_cloud(tags_q, steps=6)

        kwargs.update({
            'tag_object': self.tag_object,
            'ressources_tags': tags_q,
        })
        return kwargs

    def get(self, request, *args, **kwargs):
        self.gallery_object = self.get_gallery_object()
        self.album_object = self.get_album_object()
        self.tag_object = self.get_tag_object()
        return super(AlbumTagRessourcesView, self).get(request, *args, **kwargs)


class RessourceDetailView(AlbumConfinementMixin, TemplateView):
    """
    Display the ressources and their tags
    """
    template_name = 'porticus/ressource_detail.html'

    def get(self, request, *args, **kwargs):
        self.gallery_object = self.get_gallery_object()
        self.album_object = self.get_album_object()
        self.ressource_object = self.get_ressource_object()
        return super(RessourceDetailView, self).get(request, *args, **kwargs)
