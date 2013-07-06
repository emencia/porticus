"""Views for porticus"""
from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list

from porticus.models import Gallery
from porticus.settings import PAGINATION


def view_gallery_list(request, page=None):
    return object_list(request,
                       queryset=Gallery.published.all(),
                       paginate_by=PAGINATION, page=page)


def view_gallery_detail(request, slug, page=None):
    gallery = get_object_or_404(Gallery, slug=slug)

    return object_list(request,
                       template_name=gallery.template_name,
                       queryset=gallery.ressources.filter(
                           priority__gt=0),
                       paginate_by=PAGINATION, page=page,
                       extra_context={'gallery': gallery})
