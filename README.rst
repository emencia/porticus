.. _DjangoCMS: https://www.django-cms.org
.. _South: http://south.readthedocs.org/en/latest/
.. _mptt: https://github.com/django-mptt/django-mptt/
.. _django-tagging: https://github.com/brosner/django-tagging
.. _easy-thumbnails: https://github.com/SmileyChris/easy-thumbnails
.. _django-filer: https://github.com/stefanfoulis/django-filer

porticus
========

Yet another File gallery for Django.

**Galleries** contains **Albums** that contains **Ressources** and ressources are your files items. Usually used like an image gallery, you should also use it like a download center for many file types.

Galleries and Albums have thumbnails, Ressources have a thumbnail and a file but the file can be a real uploaded file on your server or just an url to link to. Also Ressources have optional tags.

Note that Albums make usage of `mptt`_, so Albums can have album children.

Shipped templates are basics, you probably will have to override them to suit your needs.

Migrations
**********

Since the **0.9 version**, *Django < 1.6* and *DjangoCMS < 3.0* support has been dropped and so Porticus migrations have been reseted, since we can't support migrations with *DjangoCMS < 3.0* because it will need too much time to fix them.

Requires
********

* Django >= 1.6;
* `mptt`_;
* `django-tagging`_;
* `django-filer`_;
* `easy-thumbnails`_;

Optional
---------

* `DjangoCMS`_ >= 3.0 to use Porticus with the cms plugin;
* `South`_ migration is supported. This is not required, but strongly recommended for future updates;

Install
*******

In your urls.py : ::

    url(r'^porticus/', include('porticus.urls')),

Or to point out a specific gallery : ::

    url(r'^$', 'porticus.views.view_gallery_detail', {'slug':'home-intro'}, name='homepage_gallery_detail'),

Then add the content of ``porticus.settings`` in your settings file.

In your ``INSTALLED_APPS`` setting : ::
    
    INSTALLED_APPS = (
        ...
        'mptt',
        'sorl.thumbnail',
        'porticus',
        'tagging',
        'filer',
        'easy_thumbnails',
        ...
    )

Also if you want to use its plugin within `DjangoCMS`_ add this to ``INSTALLED_APPS`` setting : ::

    'porticus.cmsplugin_porticus',

Also you can find some Sitemap classes in ``sitemaps.py`` that you can mount in your project sitemap like so : ::

    from django.conf.urls import patterns
    from porticus.sitemaps import PorticusGallerySitemap, PorticusAlbumSitemap, PorticusRessourceSitemap

    sitemaps = {
        'galleries': PorticusGallerySitemap,
        'albums': PorticusAlbumSitemap,
        'photos': PorticusRessourceSitemap,
    }

    urlpatterns = patterns('',
        # the sitemap
        (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
    )

See the `Django documentation about Sitemaps <https://docs.djangoproject.com/en/dev/ref/contrib/sitemaps/>`_ for more details.