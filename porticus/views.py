"""
Views for porticus
"""
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list

from porticus.models import Album


def view_album_list(request, page=None):
    return object_list(request, queryset=Album.published.all(), paginate_by=settings.PORTICUS_PAGINATION, page=page)


def view_album_detail(request, slug, page=None):
    album = get_object_or_404(Album, slug=slug)

    return object_list(request,
                       template_name=album.template_name,
                       queryset=album.ressources.filter(
                           priority__gt=0),
                       paginate_by=settings.PORTICUS_PAGINATION, page=page,
                       extra_context={'album': album})
