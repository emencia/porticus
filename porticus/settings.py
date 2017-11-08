"""
Settings for porticus
"""
_ = lambda s: s

PORTICUS_GALLERIES_PAGINATION = 16
PORTICUS_ALBUMS_PAGINATION = 16
PORTICUS_RESSOURCES_PAGINATION = 16

# Templates choices in the admin
PORTICUS_GALLERY_TEMPLATE_CHOICES = (
    ('porticus/gallery_detail.html', 'Default'),
)
PORTICUS_ALBUM_TEMPLATE_CHOICES = (
    ('porticus/album_detail.html', 'Default'),
)
PORTICUS_GALLERY_PLUGIN_TEMPLATE_CHOICES = (
    ('porticus/cms/gallery_detail.html', 'Default'),
)
PORTICUS_ALBUM_PLUGIN_TEMPLATE_CHOICES = (
    ('porticus/cms/album_detail.html', 'Default'),
)

# Default template choices
PORTICUS_GALLERY_TEMPLATE_DEFAULT = PORTICUS_GALLERY_TEMPLATE_CHOICES[0][0]
PORTICUS_ALBUM_TEMPLATE_DEFAULT = PORTICUS_ALBUM_TEMPLATE_CHOICES[0][0]
PORTICUS_GALLERY_PLUGIN_TEMPLATE_DEFAULT = PORTICUS_GALLERY_PLUGIN_TEMPLATE_CHOICES[0][0]
PORTICUS_ALBUM_PLUGIN_TEMPLATE_DEFAULT = PORTICUS_ALBUM_PLUGIN_TEMPLATE_CHOICES[0][0]

# Templates for templatetags
PORTICUS_ALBUM_TEMPLATE_FRAGMENT = 'porticus/templatetags/album_detail_fragment.html'
PORTICUS_GALLERIES_TEMPLATE_FRAGMENT = 'porticus/templatetags/gallery_list_fragment.html'

# Ressource file types
PORTICUS_RESSOURCE_FILETYPE_CHOICES = (
    ('image', _("Image")),
    ('video', _("Video")),
    ('binary', _("Binary")),
)
PORTICUS_RESSOURCE_FILETYPE_DEFAULT = 'image'
