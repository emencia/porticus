.. _mptt: https://github.com/django-mptt/django-mptt/
.. _sorl.thumbnail: https://github.com/sorl/sorl-thumbnail

porticus
========

Yet another File gallery for Django.

**Galleries** contains **Albums** that contains **Ressources** and ressources are your files items. Usually used like an image gallery, you should also use it like a download center for many file types.

Note that Albums make usage of `mptt`_, so Albums can have album children. Shipped templates are basic, they don't manage albums tree.

Requires
********

* `mptt`_
*  `sorl.thumbnail`_;

Install
*******

In your urls.py : ::

    url(r'^porticus/', include('porticus.urls')),

Or to point out a specific gallery : ::

    url(r'^$', 'porticus.views.view_gallery_detail', {'slug':'home-intro'}, name='homepage_gallery_detail'),

Then add the content of ``porticus.settings`` in your settings file.

In your settings.INSTALLED_APPS : ::
    
    'mptt',
    'sorl.thumbnail',
    'porticus',
    
And if you want also to use it within DjangoCMS : ::

    'porticus.cmsplugin_porticus',
