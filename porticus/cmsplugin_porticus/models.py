"""Models of porticus.cmsplugins_album"""
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from porticus.models import Gallery, Album

class GalleryPlugin(CMSPlugin):
    """CMS Plugin for displaying a Gallery"""

    gallery = models.ForeignKey(Album, verbose_name=_('album'), help_text=_('Gallery to display'))

    template_name = models.CharField(_('template'), max_length=100, help_text=_('Template used to render the plugin Album'), choices=settings.PORTICUS_GALLERY_PLUGIN_TEMPLATE_CHOICES, default=settings.PORTICUS_GALLERY_PLUGIN_TEMPLATE_DEFAULT, blank=False)

    def __unicode__(self):
        return self.gallery.name

class AlbumPlugin(CMSPlugin):
    """CMS Plugin for displaying a Album"""

    album = models.ForeignKey(Album, verbose_name=_('album'), help_text=_('Album to display'))

    template_name = models.CharField(_('template'), max_length=100, help_text=_('Template used to render the plugin Album'), choices=settings.PORTICUS_ALBUM_PLUGIN_TEMPLATE_CHOICES, default=settings.PORTICUS_ALBUM_PLUGIN_TEMPLATE_DEFAULT, blank=False)

    def __unicode__(self):
        return self.album.name
