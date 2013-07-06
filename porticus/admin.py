"""
Admin for porticus
"""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from porticus.models import Ressource, Gallery


def admin_image(obj):
    if obj.image:
        from sorl.thumbnail.shortcuts import get_thumbnail
        try:
            thumbnail = get_thumbnail(obj.image, '75x75')
        except:
            return _('Invalid image for %s') % unicode(obj)
        url = thumbnail.url
        return '<img src="%s" alt="%s" />' % (url, unicode(obj))
    else:
        return _('No image for %s') % unicode(obj)
admin_image.short_description = _('image')
admin_image.allow_tags = True


class RessourceAdmin(admin.ModelAdmin):
    ordering = ('-creation_date',)
    search_fields = ('name', 'description', 'short_description', 'slug')
    list_filter = ('file_type', 'creation_date', 'gallery')
    list_editable = ('placeholder_name',)
    list_display = (admin_image, 'name', 'file_type',
                    'get_galleries', 'placeholder_name',
                    'get_file', 'file_weight', 'priority')
    fieldsets = ((None, {'fields': ('name', 'file_type', 'image')}),
                 (_('Descriptions'), {'fields': (
                     'header', 'short_description', 'description'),
                                      'classes': ('collapse',
                                                  'collapse-closed')}),
                 (_('File'), {'fields': ('file', 'file_url'),
                              'description':
                              _('You must fill one of these fields')}),
                 (None, {'fields': ('file_weight',)}),
                 (None, {'fields': ('video',)}),
                 (None, {'fields': ('placeholder_name',)}),
                 (None, {'fields': ('template_name', 'priority', 'slug')}),)
    prepopulated_fields = {'slug': ('name', )}

    def get_galleries(self, r):
        return ', '.join([n.name for n in r.gallery_set.all()])
    get_galleries.short_description = _('galleries')


class GalleryAdmin(admin.ModelAdmin):
    ordering = ('-creation_date',)
    search_fields = ('name', 'description', 'credits',
                     'short_description', 'slug')
    list_filter = ('creation_date',)
    list_display = (admin_image, 'name', 'ressources_link', 'priority')
    fieldsets = ((None, {'fields': ('name', 'image', 'thumbnail',)}),
                 (_('Descriptions'), {'fields': (
                     'header', 'short_description',
                     'description', 'credits'),
                                      'classes': ('collapse',
                                                  'collapse-closed')}),
                 (None, {'fields': ('ressources',)}),
                 (None, {'fields': ('template_name', 'priority', 'slug')}),)
    filter_horizontal = ('ressources',)
    prepopulated_fields = {'slug': ('name', )}

    def ressources_link(self, gallery):
        links = []
        for r in gallery.ressources.all():
            links.append('<a href="/admin/gallery/ressource/%s">%s</a>' % (
                r.id, str(r)))
        return '<br />'.join(links)
    ressources_link.allow_tags = True
    ressources_link.short_description = _('Ressources')

admin.site.register(Ressource, RessourceAdmin)
admin.site.register(Gallery, GalleryAdmin)
