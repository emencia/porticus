.. _DjangoCMS: https://www.django-cms.org
.. _South: http://south.readthedocs.org/en/latest/
.. _mptt: https://github.com/django-mptt/django-mptt/
.. _django-tagging: https://github.com/brosner/django-tagging
.. _django-filebrowser: https://github.com/sehmaschine/django-filebrowser
.. _django-filebrowser-no-grappelli: https://github.com/smacker/django-filebrowser-no-grappelli

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

Links
*****

* Download his `PyPi package <http://pypi.python.org/pypi/porticus>`_;
* Clone it on his `Github repository <https://github.com/emencia/porticus>`_;

Requires
********

* Django >= 1.6;
* `mptt`_;
* `django-tagging`_;
* `django-filebrowser-no-grappelli`_ >= 3.5.6;

Optional
---------

* `DjangoCMS`_ >= 3.0 to use Porticus with the cms plugin;
* `South`_ migration is supported. This is not required, but strongly recommended for future updates;

Install
*******

In your urls.py : ::

    url(r'^porticus/', include('porticus.urls', namespace='porticus')),

Or to point out a specific gallery : ::

    url(r'^$', 'porticus.views.view_gallery_detail', {'slug':'home-intro'}, name='homepage_gallery_detail'),

Then add the content of ``porticus.settings`` in your settings file and the apps in your ``INSTALLED_APPS`` setting : ::
    
    INSTALLED_APPS = (
        ...
        'mptt',
        'sorl.thumbnail',
        'porticus',
        'tagging',
        'filebrowser',
        'easy_thumbnails',
        ...
    )

Also if you want to use its plugin within `DjangoCMS`_ add this to ``INSTALLED_APPS`` setting : ::

    'porticus.cmsplugin_porticus',

Then some `django-filebrowser`_ basic settings (see its documentation for more details) : ::

    FILEBROWSER_VERSIONS_BASEDIR = '_uploads_versions'

    FILEBROWSER_MAX_UPLOAD_SIZE = 10*1024*1024 # 10 Mb

    FILEBROWSER_NORMALIZE_FILENAME = True

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