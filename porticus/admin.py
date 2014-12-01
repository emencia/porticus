"""
Admin for porticus
"""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mptt.admin import MPTTModelAdmin

from filebrowser.settings import ADMIN_THUMBNAIL

from porticus.models import Ressource, Gallery, Album

def slide_image_thumbnail(obj):
    if obj.image and obj.image.filetype == "Image":
        return '<img src="%s" />' % obj.image.version_generate(ADMIN_THUMBNAIL).url
    else:
        return _('No image for %s') % unicode(obj)
slide_image_thumbnail.short_description = _('image')
slide_image_thumbnail.allow_tags = True


class GalleryAdmin(admin.ModelAdmin):
    ordering = ('-creation_date',)
    search_fields = ('name', 'description', 'slug')
    list_filter = ('creation_date', 'publish')
    list_editable = ('priority', 'publish', 'template_name')
    list_display = (slide_image_thumbnail, 'name', 'publish', 'priority', 'template_name')
    list_display_links = (slide_image_thumbnail, 'name')
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
    ordering = ('album', 'priority')
    search_fields = ('name', 'description', 'slug')
    list_filter = ('file_type', 'creation_date', 'album', 'publish')
    list_editable = ('priority', 'publish')
    list_display = (slide_image_thumbnail, 'album', 'name', 'publish', 'priority', 'file_type')
    filter_horizontal = ('related',)
    prepopulated_fields = {'slug': ('name', )}
    fieldsets = (
        (None, {
            'fields': ('album', 'publish', 'priority'),
        }),
        (None, {
            'fields': ('name', 'slug', 'image'),
        }),
        (_('File'), {
            'fields': ('file_type', 'file', 'file_url'), 
            'description': _('You must fill one of these fields'),
        }),
        (None, {
            'fields': ('description',),
        }),
        (_('Relations'), {
            'classes': ('collapse',),
            'fields': ('tags', 'related',),
        }),
    )


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Ressource, RessourceAdmin)
