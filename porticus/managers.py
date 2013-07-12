"""Model managers for porticus"""
from django.db import models

class RessourcePublishedManager(models.Manager):
    """Manager for Ressource model"""
    def get_query_set(self):
        return super(RessourcePublishedManager, self).get_query_set().filter(priority__gt=0)


class GalleryPublishedManager(models.Manager):
    """Manager for Gallery model"""
    def get_query_set(self):
        return super(GalleryPublishedManager, self).get_query_set().filter(priority__gt=0)


class AlbumPublishedManager(models.Manager):
    """Manager for Album model"""
    def get_query_set(self):
        return super(AlbumPublishedManager, self).get_query_set().filter(priority__gt=0)
