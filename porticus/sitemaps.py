# -*- coding: utf-8 -*-
"""
Sitemap entries

Only published entries are exposed.

* Album last modification datetime is the newest creation date either from
  album or its ressources;
* Ressource that don't have an uploaded file are not exposed;

Exposing Ressources can turn into a very big 'sitemap.xml' file if you have
many Ressources, be careful.
"""
import datetime

from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from porticus.models import Gallery, Album, Ressource


class PorticusGallerySitemap(Sitemap):
    changefreq = "monthly"
    priority = 1.0

    def items(self):
        return models.Gallery.published.order_by('priority', 'name')

    def location(self, obj):
        return reverse('porticus:gallery-detail', kwargs={
            'gallery_slug': obj.slug,
        })

    def lastmod(self, obj):
        return obj.created


class PorticusAlbumSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return models.Album.objects.filter(publish=True).order_by('priority',
                                                                  'name')

    def location(self, obj):
        return reverse('porticus:album-detail', kwargs={
            'gallery_slug': obj.gallery.slug,
            'album_slug': obj.slug,
        })

    def lastmod(self, obj):
        """
        Return the youngest datetime between "object creation date" and
        ressources "creation dates", so if there are a more young ressource
        entry than the album, the Album will exposes it
        """
        ressources_dates = list(obj.ressource_set.all().values_list('created',
                                                                    flat=True))
        return max([obj.created] + ressources_dates)


class PorticusRessourceSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.4

    def items(self):
        """
        Only exposes those ressources that have an uploaded file, excludes
        those ones that have only a filled 'file_url'
        """
        return models.Ressource.published.exclude(file='').order_by('priority',
                                                                    'name')

    def location(self, obj):
        return obj.file.url

    def lastmod(self, obj):
        return obj.created
