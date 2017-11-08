from django.db import models


class RessourcePublishedManager(models.Manager):
    """Manager for Ressource model"""
    def get_queryset(self):
        return super(RessourcePublishedManager, self).get_queryset().filter(publish=True)


class GalleryPublishedManager(models.Manager):
    """Manager for Gallery model"""
    def get_queryset(self):
        return super(GalleryPublishedManager, self).get_queryset().filter(publish=True)


class AlbumPublishedManager(models.Manager):
    """Manager for Album model"""
    def get_queryset(self):
        return super(AlbumPublishedManager, self).get_queryset().filter(publish=True)
