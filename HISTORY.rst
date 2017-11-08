
=========
Changelog
=========

Version 2.0.0 - Unreleased
--------------------------

Added Django>=1.9 compatibility, dropped Django<=1.9 support and contains some backward incompatible changes on migrations, models and all, so **your not advised to migrate your old installs to this version**.

* Migrations has been reset;


Version 1.1.4 - 2016/10/19
--------------------------

* Fixed error from previous commit that was causing error for existing tags;

Version 1.1.3 - 2016/10/19
--------------------------

* Fixed ``AlbumTagRessourcesView`` view raising an error 500 because of DoesNotExist exception when tag does not exist, instead raise a 404;

Version 1.1.2 - 2016/09/30
--------------------------

* Fixed missing migration;

Version 1.1.1 - 2016/09/20
--------------------------

* Prepopulate slug for Ressource inline for master branch, close #12;

Version 1.1.0 - 2016/05/25
--------------------------

* Dropped usage 'auto_add_now' from all model 'creation_date' field, instead fill these fields from model save method, added migration for this change;

Version 1.0.2 - 2016/05/14
--------------------------

* Fixed Warning on model field Ressource.related, added migration to follow this change, close #11;

Version 1.0.1 - 2015/11/09
--------------------------

* Fixed Pypi classifiers in setup.py;
* Fixed README;

Version 1.0.0 - 2015/11/08
--------------------------

* Dropped support for Django<=1.7;
* moved South migration directory to 'south_migrations' so they still be usable with South==1.0.0;
* Update setup.py for better Pypi classifiers


Version 0.9.6 - 2014/12/01
--------------------------

* Deleting field 'Ressource.file_weight' that was unused;
* Adding unique constraint on 'Ressource', fields ['album', 'slug'] so the ressource slug is unique within an Album;
* Better 'admin.RessourceAdmin';

Version 0.9.5 - 2014/11/06
--------------------------

* Remove cmsplugin code from this repo, the plugin has its own repo named 'cmsplugin_porticus';
* update README;

Version 0.9.4 - 2014/10/27
--------------------------

* Remove mptt admin template that was containing an old fix for mptt<0.6;
* Fix README

Version 0.9.3 - 2014/10/26
--------------------------

* Remove easy-thumbnails and django-filer usage in profit of django-filebrowser-no-grapelli;
* Update migrations;
* Changing templates to suit changing for filebrowser;


Version 0.9.2 - 2014/10/15
--------------------------

* Add url namespace 'porticus' usage;
* update README;

Version 0.9.1 - 2014/10/15
--------------------------

* Minor update to put usefull links in README;

Version 0.9 - 2014/10/15
------------------------

* Drop support for Django<1.6 and DjangoCMS<3.0;
* Add support for Django>=1.6 and DjangoCMS>=3.0;
* Remove past migrations that are not compatible with DjangoCMS>=3.0;
* Add django-filer usage to manage files in models;
* Add easy-thumbnails usage instead of sorl.thumbnails;


Version 0.8.1 - 2014/10/14
--------------------------

* Add cloud tags in AlbumTagRessourcesView and its template;

Version 0.8.0 - 2014/10/09
--------------------------

* Embed a diff patch for django-logging issue with sqlite and mysql for some specific API usage like with TaggedItem.objects.get_by_model
* Adapt template and view for album's and galleries slug name changes;
* Fixed views to nicely filter tag/tagitem's queryset;
* Remove tagging templatetag use in profit of code in views;


Version 0.7.7 - 2014/10/08
--------------------------

* Remove uneeded 'tags' fields on Album and Gallery models;
* correct some templates;
* Recreate migrations;
* some fixes in templates;
* disable FileBrowseField usage for now;

Version 0.7.5 - 2014/07/05
--------------------------

* Re-enable the Album published manager;
* add support for Django sitemaps;
* update README;


Version 0.7.4 - 2014/05/29
--------------------------

* Add a default choice to Ressource file type;


Version 0.7.3 - 2014/05/29
--------------------------

* Moves Ressource filetype choices in settings;
* add South support;


Version 0.7.2 - 2014/05/27
--------------------------

* Remove get_absolute_url that cause troubles with specific integration (url mounted for specific album and disable all porticus common urls) until i find how to determine its usage from settings option.
