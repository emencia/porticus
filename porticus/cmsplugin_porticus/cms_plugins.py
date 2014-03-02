"""
DjangoCMS plugin for porticus
"""
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from porticus.cmsplugin_album.models import AlbumPlugin as AlbumPluginModel


class AlbumPlugin(CMSPluginBase):
    module = 'Porticus'
    model = AlbumPluginModel
    name = _('Album')
    fields = ('album', 'template_name')
    render_template = 'album/cms/album_detail.html'

    def render(self, context, instance, placeholder):
        """Update the context with plugin's data"""
        context.update({
            'object': instance,
            'placeholder': placeholder
        })
        return context


plugin_pool.register_plugin(AlbumPlugin)
