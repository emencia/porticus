"""
Admin for porticus
"""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mptt.admin import MPTTModelAdmin

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


class GalleryAdmin(admin.ModelAdmin):
    ordering = ('-creation_date',)
    search_fields = ('name', 'description', 'slug')
    list_filter = ('creation_date', 'publish')
    list_editable = ('priority', 'publish', 'template_name')
    list_display = (admin_image, 'name', 'publish', 'priority', 'template_name')
    list_display_links = (admin_image, 'name')
    prepopulated_fields = {'slug': ('name', )}
    fieldsets = (
        (None, {
            'fields': ('name', 'image')
        }),
        (None, {
            'fields': ('publish', 'template_name', 'priority', 'slug')
        }),
        (None, {
            'fields': ('description',),
        }),
    )


class RessourceInline(admin.StackedInline):
    model = Ressource
    ordering = ('priority', 'name')


class AlbumAdmin(MPTTModelAdmin):
    ordering = ('-creation_date',)
    search_fields = ('name', 'description', 'slug')
    list_filter = ('creation_date', 'gallery', 'publish')
    list_editable = ('priority', 'publish', 'template_name')
    list_display = ('name', 'slug', 'publish', 'priority', 'template_name', 'ressources_count')
    fieldsets = (
        (None, {
            'fields': ('gallery','parent',)
        }),
        (None, {
            'fields': ('name', 'image',)
        }),
        (None, {
            'fields': ('publish', 'template_name', 'priority', 'slug')
        }),
        (None, {
            'fields': ('description',),
        }),
    )
    prepopulated_fields = {'slug': ('name', )}
    inlines = [
        RessourceInline,
    ]
    mptt_level_indent = 25

    def ressources_count(self, album):
        return album.ressource_set.all().count()
    ressources_count.short_description = _('Ressources')


class RessourceAdmin(admin.ModelAdmin):
    ordering = ('-creation_date',)
    search_fields = ('name', 'description')
    list_filter = ('file_type', 'creation_date', 'album', 'publish')
    list_editable = ('priority', 'publish')
    list_display = (admin_image, 'album', 'name', 'publish', 'priority', 'file_type', 'file_weight')
    fieldsets = (
        (None, {
            'fields': ('album',),
        }),
        (None, {
            'fields': ('publish', 'priority'),
        }),
        (None, {
            'fields': ('name', 'image'),
        }),
        (_('File'), {
            'fields': ('file_type', 'file', 'file_url', 'file_weight'), 
            'description': _('You must fill one of these fields'),
        }),
        (None, {
            'fields': ('description',),
        }),
    )


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Ressource, RessourceAdmin)
