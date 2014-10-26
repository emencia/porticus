"""
Settings for porticus
"""
gettext = lambda s: s

PORTICUS_GALLERIES_PAGINATION = PORTICUS_ALBUMS_PAGINATION = PORTICUS_RESSOURCES_PAGINATION = 16

# Templates choices in the admin
PORTICUS_GALLERY_TEMPLATE_CHOICES = (
    ('porticus/gallery_detail.html', 'Default template'),
)
PORTICUS_ALBUM_TEMPLATE_CHOICES = (
    ('porticus/album_detail.html', 'Default template'),
)
PORTICUS_GALLERY_PLUGIN_TEMPLATE_CHOICES = (
    ('porticus/cms/gallery_detail.html', 'Default template'),
)
PORTICUS_ALBUM_PLUGIN_TEMPLATE_CHOICES = (
    ('porticus/cms/album_detail.html', 'Default template'),
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
PORTICUS_RESSOURCE_FILETYPES = (
    (0, 'binary'),
    (1, 'image'),
    (2, "youtube"),
)
PORTICUS_RESSOURCE_FILETYPE_CHOICES = (
    (0, gettext('Binary')),
    (1, gettext('Image')),
    (2, gettext("Youtube (only with 'file_url') usage")),
)
PORTICUS_RESSOURCE_FILETYPE_DEFAULT = 1
