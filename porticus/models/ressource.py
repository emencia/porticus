from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

from porticus.managers import RessourcePublishedManager

from filebrowser.fields import FileBrowseField

from tagging.fields import TagField
from tagging.models import Tag


PUBLISHED_CHOICES = (
    (True, _('Published')),
    (False, _('Unpublished')),
)


def get_ressource_filetype_choices():
    return settings.PORTICUS_RESSOURCE_FILETYPE_CHOICES


def get_ressource_filetype_default():
    return settings.PORTICUS_RESSOURCE_FILETYPE_DEFAULT


@python_2_unicode_compatible
class Ressource(models.Model):
    """Model for representing a ressource"""
    created = models.DateTimeField(
        _('created'),
        blank=True,
        editable=False
    )
    album = models.ForeignKey('porticus.Album')
    related = models.ManyToManyField(
        "self",
        blank=True
    )
    name = models.CharField(
        _('name'),
        max_length=250
    )
    slug = models.SlugField(
        _('slug'),
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
    description = models.TextField(
        _('description'),
        blank=True
    )
    image = FileBrowseField(
        _('image'),
        max_length=255,
        null=True,
        blank=True,
        default=None,
    )
    file_type = models.CharField(
        _('file type'),
        max_length=55,
        choices=get_ressource_filetype_choices(),
        default=get_ressource_filetype_default()
    )
    file = FileBrowseField(
        _('file'),
        max_length=255,
        null=True,
        blank=True,
        default=None,
    )
    file_url = models.URLField(
        _('file url'),
        blank=True,
    )
    tags = TagField(_('tags'))

    objects = models.Manager()
    published = RessourcePublishedManager()

    def __str__(self):
        return self.name

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    @property
    def get_file(self):
        """
        Main method to get the attached file without to search with file
        object and file_url
        """
        fileobject = None
        if self.file:
            fileobject = self.file.url

        try:
            return self.file_url or fileobject
        except ValueError:
            return None
        except AttributeError:
            return None

    def clean(self):
        if not self.get_file:
            raise ValidationError(_('Please upload a file or give a file url'))

    def save(self, *args, **kwargs):
        # First creation
        if not self.created:
            self.created = timezone.now()

        super(Ressource, self).save(*args, **kwargs)

    class Meta:
        ordering = ('album', 'priority')
        verbose_name = _('ressource')
        verbose_name_plural = _('ressources')
        unique_together = ("album", "slug")
