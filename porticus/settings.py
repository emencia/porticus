"""Settings for porticus"""
from django.conf import settings


PAGINATION = getattr(settings, 'GALLERY_PAGINATION', 10)

RESSOURCE_TEMPLATE_CHOICES = getattr(settings,
                                     'GALLERY_RESSOURCE_TEMPLATE_CHOICES',
                                     (('porticus/ressource_detail.html',
                                       'Default template'),),)

GALLERY_TEMPLATE_CHOICES = getattr(settings,
                                   'GALLERY_GALLERY_TEMPLATE_CHOICES',
                                   (('porticus/gallery_detail.html',
                                     'Default template'),),)

GALLERY_PLUGIN_TEMPLATE_CHOICES = getattr(settings,
                                          'GALLERY_GALLERY_PLUGIN_TEMPLATE_CHOICES',
                                          (('porticus/cms/gallery_detail.html',
                                            'Default template'),),)
