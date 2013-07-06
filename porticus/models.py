"""
Models for porticus
"""
from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from porticus.managers import RessourcePublishedManager, GalleryPublishedManager


class Ressource(models.Model):
    """Model for representing a ressource"""
    FILETYPE_CHOICES = ((0, _('Binary')),
                        (1, _('Image')),
                        (2, _('Text')),)

    name = models.CharField(_('name'), max_length=250)
    header = models.TextField(_('header'), blank=True)

    short_description = models.TextField(_('short description'), blank=True)
    description = models.TextField(_('description'), blank=True)
    image = models.ImageField(_('image'), blank=True,
                              upload_to='gallery/ressources/images')

    file_type = models.IntegerField(_('file type'), choices=FILETYPE_CHOICES)
    file = models.FileField(_('file'), blank=True,
                                upload_to='gallery/ressources/files')
    file_url = models.URLField(_('file url'), blank=True)
    file_weight = models.CharField(_('file weight'), blank=True,
                                   max_length=15)
    video = models.TextField(_('video'), blank=True)

    template_name = models.CharField(_('template'), max_length=255,
                                     help_text=_('Template used to render the ressource'),
                                     choices=settings.PORTICUS_RESSOURCE_TEMPLATE_CHOICES)

    priority = models.IntegerField(_('display priority'), default=100,
                    help_text=_('Set this value to 0 will hide the item'))
    placeholder_name = models.CharField(_('placeholder name'), max_length=250,
                                        blank=True, help_text=_('Used for positioning.'))

    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)
    slug = models.SlugField(_('slug'), unique=True, max_length=100)

    objects = models.Manager()
    published = RessourcePublishedManager()

    @property
    def get_file(self):
        try:
            return self.file_url or self.file.url
        except ValueError:
            return None

    def clean(self):
        if not self.get_file:
            raise ValidationError(
                _('Please fill a file or a file url'))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-priority', 'name')
        verbose_name = _('ressource')
        verbose_name_plural = _('ressources')


class Gallery(models.Model):
    """Model representing a gallery"""

    name = models.CharField(_('name'), max_length=250)
    header = models.TextField(_('header'), blank=True)

    description = models.TextField(_('description'), blank=True)
    short_description = models.TextField(_('short description'), blank=True)
    credits = models.TextField(_('credits'), blank=True)

    image = models.ImageField(_('image'), upload_to='gallery/gallery',
                              blank=True)
    thumbnail = models.ImageField(_('thumbnail'), upload_to='gallery/gallery/thumbs',
                                  blank=True)

    template_name = models.CharField(_('template'), max_length=255,
                                     help_text=_('Template used to render the gallery'),
                                     choices=settings.PORTICUS_GALLERY_TEMPLATE_CHOICES)

    ressources = models.ManyToManyField(Ressource,
                                        verbose_name=_('ressources'))

    priority = models.IntegerField(_('display priority'), default=100,
                                   help_text=_('Set this value to 0 will hide the item'))

    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)

    slug = models.SlugField(_('slug'), unique=True, max_length=100)

    objects = models.Manager()
    published = GalleryPublishedManager()

    @models.permalink
    def get_absolute_url(self):
        return ('gallery_gallery_detail', (self.slug,))

    @property
    def previous(self):
        """Return the previous gallery"""
        galleries = Gallery.published.filter(
            priority__lt=self.priority)[:1]
        if galleries:
            return galleries[0]

    @property
    def next(self):
        """Return the next gallery"""
        galleries = Gallery.published.filter(
            priority__gt=self.priority).order_by('priority')[:1]
        if galleries:
            return galleries[0]

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-priority', 'name')
        verbose_name = _('gallery')
        verbose_name_plural = _('galleries')
