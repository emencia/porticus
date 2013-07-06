"""Models of porticus.cmsplugins_gallery"""
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from porticus.models import Gallery


class GalleryPlugin(CMSPlugin):
    """CMS Plugin for displaying a Gallery"""

    gallery = models.ForeignKey(Gallery, verbose_name=_('gallery'),
                                help_text=_('Gallery to display'))

    template_name = models.CharField(_('template'), max_length=255,
                                     help_text=_('Template used to render the plugin Gallery'),
                                     choices=settings.PORTICUS_GALLERY_PLUGIN_TEMPLATE_CHOICES)

    def __unicode__(self):
        return self.gallery.name

    @property
    def render_template(self):
        """Override render_template to use
        the template_to_render attribute"""
        return self.template_name
