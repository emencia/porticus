"""
DjangoCMS plugin for porticus
"""
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from porticus.cmsplugin_gallery.models import GalleryPlugin


class CMSGalleryPlugin(CMSPluginBase):
    module = _('gallery')
    model = GalleryPlugin
    name = _('Gallery')
    fields = ('gallery', 'template_name')
    render_template = 'gallery/cms/gallery_detail.html'

    def render(self, context, instance, placeholder):
        """Update the context with plugin's data"""
        context.update({'object': instance,
                        'placeholder': placeholder})
        return context


plugin_pool.register_plugin(CMSGalleryPlugin)
