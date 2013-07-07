"""
Default settings for porticus to include in your project settings
"""

PORTICUS_PAGINATION = 10

# Default templates choices in the admin
PORTICUS_RESSOURCE_TEMPLATE_CHOICES = (
    ('porticus/ressource_detail.html', 'Default template'),
)
PORTICUS_ALBUM_TEMPLATE_CHOICES = (
    ('porticus/album_detail.html', 'Default template'),
)
PORTICUS_GALLERY_TEMPLATE_CHOICES = (
    ('porticus/gallery_detail.html', 'Default template'),
)
PORTICUS_ALBUM_PLUGIN_TEMPLATE_CHOICES = (
    ('porticus/cms/album_detail.html', 'Default template'),
)

PORTICUS_ALBUM_FRAGMENT_TEMPLATE = 'porticus/album_detail_fragment.html'
