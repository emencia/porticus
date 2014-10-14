"""Toolbar extensions for CMS"""
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool


class PorticusToolbar(CMSToolbar):

    def populate(self):
        porticus_menu = self.toolbar.get_or_create_menu(
            'porticus-menu', _('Porticus'))

        url = reverse('admin:porticus_gallery_add')
        porticus_menu.add_sideframe_item(_('New gallery'), url=url)

        url = reverse('admin:porticus_album_add')
        porticus_menu.add_sideframe_item(_('New album'), url=url)

        url = reverse('admin:porticus_ressource_add')
        porticus_menu.add_sideframe_item(_('New ressource'), url=url)

        porticus_menu.add_break()

        url = reverse('admin:porticus_gallery_changelist')
        porticus_menu.add_sideframe_item(_('Galleries list'), url=url)

        url = reverse('admin:porticus_album_changelist')
        porticus_menu.add_sideframe_item(_('Albums list'), url=url)

        url = reverse('admin:porticus_ressource_changelist')
        porticus_menu.add_sideframe_item(_('Ressources list'), url=url)

        porticus_menu.add_break()

        url = reverse('admin:tagging_tag_changelist')
        porticus_menu.add_sideframe_item(_('Tags list'), url=url)


toolbar_pool.register(PorticusToolbar)
