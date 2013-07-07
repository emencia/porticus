"""
Admin for porticus
"""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail.shortcuts import get_thumbnail

from porticus.models import Ressource, Gallery, Album

def admin_image(obj):
    if obj.image:
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
    list_filter = ('file_type', 'creation_date', 'album')
    list_editable = ('placeholder_name',)
    list_display = (admin_image, 'name', 'file_type',
                    'get_albums', 'placeholder_name',
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

    def get_albums(self, r):
        return ', '.join([n.name for n in r.album_set.all()])
    get_albums.short_description = _('albums')


class GalleryAdmin(admin.ModelAdmin):
    ordering = ('-creation_date',)
    search_fields = ('name', 'description', 'short_description', 'slug')
    list_filter = ('creation_date',)
    list_display = (admin_image, 'name', 'priority')
    fieldsets = ((None, {'fields': ('name', 'image', 'thumbnail',)}),
                 (_('Descriptions'), {'fields': ('short_description', 'description'),
                                      'classes': ('collapse', 'collapse-closed')}),
                 (None, {'fields': ('template_name', 'priority', 'slug')}),)
    prepopulated_fields = {'slug': ('name', )}


class AlbumAdmin(admin.ModelAdmin):
    ordering = ('-creation_date',)
    search_fields = ('name', 'description', 'short_description', 'slug')
    list_filter = ('creation_date',)
    list_display = (admin_image, 'name', 'ressources_link', 'priority')
    fieldsets = ((None, {'fields': ('gallery',)}),
                (None, {'fields': ('name', 'image', 'thumbnail',)}),
                (_('Descriptions'), {'fields': ('short_description', 'description'),
                                      'classes': ('collapse', 'collapse-closed')}),
                (None, {'fields': ('ressources',)}),
                (None, {'fields': ('template_name', 'priority', 'slug')}),)
    filter_horizontal = ('ressources',)
    prepopulated_fields = {'slug': ('name', )}

    def ressources_link(self, album):
        links = []
        for r in album.ressources.all():
            links.append('<a href="/admin/porticus/ressource/%s">%s</a>' % (r.id, str(r)))
        return '<br />'.join(links)
    ressources_link.allow_tags = True
    ressources_link.short_description = _('Ressources')

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Ressource, RessourceAdmin)
