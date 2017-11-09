.. _mptt: https://github.com/django-mptt/django-mptt/
.. _django-tagging: https://github.com/brosner/django-tagging
.. _django-filebrowser-no-grappelli: https://github.com/smacker/django-filebrowser-no-grappelli
.. _cmsplugin_porticus: https://github.com/emencia/cmsplugin_porticus

Porticus
========

Yet another File gallery for Django.

**Galleries** contains **Albums** that contains **Ressources** and ressources are your files items. Usually used like an image gallery, you should also use it like a download center for many file types.

Galleries and Albums have thumbnails, Ressources have a thumbnail and a file but the file can be a real uploaded file on your server or just an url to link to. Also Ressources have optional tags.

Note that Albums make usage of `mptt`_, so Albums can have album children.

Shipped templates are basics, you probably will have to override them to suit your needs.

Links
*****

* Download his `PyPi package <http://pypi.python.org/pypi/porticus>`_;
* Clone it on his `Github repository <https://github.com/emencia/porticus>`_;

Requires
********

* Django >= 1.9;
* `mptt`_;
* `django-tagging`_;
* `django-filebrowser-no-grappelli`_;

And optionnally ``djangocms_text_ckeditor`` to use ``TextEditorWidget`` on gallery, album and ressource descriptions. If not, simple Textarea widget is used instead.

Install
*******

Install package from PyPi: ::

    pip install porticus

In your urls.py : ::

    url(r'^porticus/', include('porticus.urls', namespace='porticus')),

Or to point out a specific gallery : ::

    url(r'^$', 'porticus.views.view_gallery_detail', {'slug':'home-intro'}, name='homepage_gallery_detail'),

Then add the content of ``porticus.settings`` in your settings file and the apps in your ``INSTALLED_APPS`` setting : ::

    INSTALLED_APPS = (
        ...
        'mptt',
        'tagging',
        'filebrowser',
        'porticus',
        ...
    )

Then add its settings : ::

    from porticus.settings import *


See included application file ``settings.py`` to know more about available settings you can override.

Then some `django-filebrowser-no-grappelli`_ basic settings (see its documentation for more details) : ::

    FILEBROWSER_VERSIONS_BASEDIR = '_uploads_versions'

    FILEBROWSER_MAX_UPLOAD_SIZE = 10*1024*1024 # 10 Mb

    FILEBROWSER_NORMALIZE_FILENAME = True

And finally apply migrations.

Also you can find some Sitemap classes in ``sitemaps.py`` that you can mount in your project sitemap like so : ::

    from django.conf.urls import url
    from porticus.sitemaps import PorticusGallerySitemap, PorticusAlbumSitemap, PorticusRessourceSitemap

    sitemaps = {
        'galleries': PorticusGallerySitemap,
        'albums': PorticusAlbumSitemap,
        'photos': PorticusRessourceSitemap,
    }

    urlpatterns = [
        # Sitemap
        url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
    ]

See the `Django documentation about Sitemaps <https://docs.djangoproject.com/en/dev/ref/contrib/sitemaps/>`_ for more details.
