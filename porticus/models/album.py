from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

from porticus.managers import AlbumPublishedManager

from mptt.models import MPTTModel, TreeForeignKey, TreeManager

from filebrowser.fields import FileBrowseField

from tagging.models import Tag


PUBLISHED_CHOICES = (
    (True, _('Published')),
    (False, _('Unpublished')),
)


def get_album_template_choices():
    return settings.PORTICUS_ALBUM_TEMPLATE_CHOICES


def get_album_template_default():
    return settings.PORTICUS_ALBUM_TEMPLATE_DEFAULT


@python_2_unicode_compatible
class Album(MPTTModel):
    """Model representing an album"""
    created = models.DateTimeField(
        _('created'),
        blank=True,
        editable=False
    )
    gallery = models.ForeignKey('porticus.Gallery')
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children'
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
        choices=get_album_template_choices(),
        default=get_album_template_default()
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

    objects = TreeManager()
    published = AlbumPublishedManager()

    def __str__(self):
        return self.name

    def get_tags(self):
        """
        Return a queryset of tags used from album's ressources
        """
        return Tag.objects.get_for_object(self)

    def get_published_children(self):
        """
        Return all ressources for the album and all its children
        """
        return self.get_children().filter(publish=True)

    def get_published_descendants(self):
        """
        Return all ressources for the album and its direct descendants
        """
        return self.get_descendants().filter(publish=True)

    def get_published_ressources(self):
        """
        Return all ressources for the album
        """
        return self.ressource_set.filter(publish=True).order_by('priority',
                                                                'name')

    def save(self, *args, **kwargs):
        # First creation
        if not self.created:
            self.created = timezone.now()

        super(Album, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('album')
        verbose_name_plural = _('albums')

    class MPTTMeta:
        order_insertion_by = ['gallery', 'priority', 'name']
