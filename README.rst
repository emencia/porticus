porticus
========

Yet another File gallery for Django

In your urls.py : ::

    url(r'^porticus/', include('parrotzik.porticus.urls')),

Or to point out a specific gallery : ::

    url(r'^$', 'porticus.views.view_gallery_detail', {'slug':'home-intro'}, name='homepage_gallery_detail'),


In your settings.INSTALLED_APPS : ::

    #'sorl.thumbnail',
    'parrotzik.porticus',
    'parrotzik.porticus.cmsplugin_porticus',
