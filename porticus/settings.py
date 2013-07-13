"""
Settings for porticus
"""

PORTICUS_GALLERIES_PAGINATION = PORTICUS_ALBUMS_PAGINATION = PORTICUS_RESSOURCES_PAGINATION = 16

# Default templates choices in the admin
PORTICUS_GALLERY_TEMPLATE_CHOICES = (
    ('porticus/gallery_detail.html', 'Default template'),
)
PORTICUS_ALBUM_TEMPLATE_CHOICES = (
    ('porticus/album_detail.html', 'Default template'),
)
PORTICUS_ALBUM_PLUGIN_TEMPLATE_CHOICES = (
    ('porticus/cms/album_detail.html', 'Default template'),
)

# Default templates for templatetags
PORTICUS_ALBUM_TEMPLATE_FRAGMENT = 'porticus/templatetags/album_detail_fragment.html'
PORTICUS_GALLERIES_TEMPLATE_FRAGMENT = 'porticus/templatetags/gallery_list_fragment.html'
