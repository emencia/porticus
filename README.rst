porticus
========

Yet another File gallery for Django. **Galleries** contains **Albums** that contains **Ressources** and ressources is your files items. Usually used like an image gallery, you can also use it like a download center for many file types.

In your urls.py : ::

    url(r'^porticus/', include('porticus.urls')),

Or to point out a specific gallery : ::

    url(r'^$', 'porticus.views.view_gallery_detail', {'slug':'home-intro'}, name='homepage_gallery_detail'),

Then add the content of ``porticus.settings`` in your settings file.

In your settings.INSTALLED_APPS : ::

    'porticus',
    'porticus.cmsplugin_porticus',
