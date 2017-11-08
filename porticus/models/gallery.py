from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

from porticus.managers import GalleryPublishedManager

from filebrowser.fields import FileBrowseField

from tagging.models import Tag


PUBLISHED_CHOICES = (
    (True, _('Published')),
    (False, _('Unpublished')),
)


def get_gallery_template_choices():
    return settings.PORTICUS_GALLERY_TEMPLATE_CHOICES


def get_gallery_template_default():
    return settings.PORTICUS_GALLERY_TEMPLATE_DEFAULT


@python_2_unicode_compatible
class Gallery(models.Model):
    """Model representing a gallery"""
    created = models.DateTimeField(
        _('created'),
        blank=True,
        editable=False
    )
    name = models.CharField(
        _('name'),
        max_length=250
    )
    slug = models.SlugField(
        _('slug'),
        unique=True,
        max_length=100
    )
    publish = models.BooleanField(
        _('published'),
        choices=PUBLISHED_CHOICES,
        default=True
    )
    priority = models.IntegerField(
        _('display priority'),
        default=100
    )
    template_name = models.CharField(
        _('template'),
        max_length=255,
        choices=get_gallery_template_choices(),
        default=get_gallery_template_default()
    )
    description = models.TextField(
        _('description'),
        blank=True
    )
    image = FileBrowseField(
        _('image'),
        max_length=255,
        null=True,
        blank=True,
        default=None
    )

    objects = models.Manager()
    published = GalleryPublishedManager()

    def __str__(self):
        return self.name

    def get_tags(self):
        """
        Return a queryset of tags used from gallery's ressources (from the
        gallery's albums)
        """
        return Tag.objects.get_for_object(self)

    def save(self, *args, **kwargs):
        # First creation
        if not self.created:
            self.created = timezone.now()

        super(Gallery, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-priority', 'name')
        verbose_name = _('gallery')
        verbose_name_plural = _('galleries')
