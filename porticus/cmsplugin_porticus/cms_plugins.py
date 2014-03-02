"""
DjangoCMS plugin for porticus
"""
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from porticus.cmsplugin_album.models import GalleryPlugin as GalleryPluginModel
from porticus.cmsplugin_album.models import AlbumPlugin as AlbumPluginModel

class PorticusPluginBase(CMSPluginBase):
    module = 'Porticus'

class GalleryPlugin(PorticusPluginBase):
    """
    Standard plugin to embed a slideshow
    """
    model = GalleryPluginModel
    name = _('Gallery')
    render_template = settings.PORTICUS_GALLERY_PLUGIN_TEMPLATE_DEFAULT

    def render(self, context, instance, placeholder):
        self.render_template = instance.template_name
        
        context.update({
            'instance': instance,
            'gallery_instance': instance.gallery,
        })
        return context

class AlbumPlugin(PorticusPluginBase):
    """
    Standard plugin to embed a slideshow
    """
    model = AlbumPluginModel
    name = _('Album')
    fields = ('album', 'template_name')
    render_template = settings.PORTICUS_ALBUM_PLUGIN_TEMPLATE_DEFAULT

    def render(self, context, instance, placeholder):
        self.render_template = instance.template_name
        
        context.update({
            'instance': instance,
            'album_instance': instance.album,
            'gallery_instance': instance.album.gallery,
        })
        return context


plugin_pool.register_plugin(GalleryPlugin)
plugin_pool.register_plugin(AlbumPlugin)
