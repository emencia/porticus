# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
import filebrowser.fields
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('image', filebrowser.fields.FileBrowseField(default=None, max_length=255, null=True, verbose_name='image', blank=True)),
                ('template_name', models.CharField(default=b'porticus/album_detail.html', help_text='Template used to render the album', max_length=255, verbose_name='template', choices=[(b'porticus/album_detail.html', b'Album template to display its ressources (default)')])),
                ('publish', models.BooleanField(default=True, verbose_name='published', choices=[(True, 'Published'), (False, 'Unpublished')])),
                ('priority', models.IntegerField(default=100, verbose_name='display priority')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='slug')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
            ],
            options={
                'verbose_name': 'album',
                'verbose_name_plural': 'albums',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('image', filebrowser.fields.FileBrowseField(default=None, max_length=255, null=True, verbose_name='image', blank=True)),
                ('template_name', models.CharField(default=b'porticus/gallery_detail.html', help_text='Template used to render the gallery', max_length=255, verbose_name='template', choices=[(b'porticus/gallery_detail.html', b'Default template')])),
                ('publish', models.BooleanField(default=True, verbose_name='published', choices=[(True, 'Published'), (False, 'Unpublished')])),
                ('priority', models.IntegerField(default=100, verbose_name='display priority')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='slug')),
            ],
            options={
                'ordering': ('-priority', 'name'),
                'verbose_name': 'gallery',
                'verbose_name_plural': 'galleries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ressource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('image', filebrowser.fields.FileBrowseField(default=None, max_length=255, blank=True, help_text='Mainly used as a thumbnails', null=True, verbose_name='image')),
                ('file_type', models.IntegerField(default=1, verbose_name='file type', choices=[(0, b'Binary'), (1, b'Image'), (2, b'Youtube (only on file url)')])),
                ('file', filebrowser.fields.FileBrowseField(default=None, max_length=255, blank=True, help_text='Mainly used for original size image or a file to download', null=True, verbose_name='file')),
                ('file_url', models.URLField(help_text="Same meaning that 'file' attribute but for an external file to use instead", verbose_name='file url', blank=True)),
                ('publish', models.BooleanField(default=True, verbose_name='published', choices=[(True, 'Published'), (False, 'Unpublished')])),
                ('priority', models.IntegerField(default=100, verbose_name='display priority')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('slug', models.SlugField(max_length=100, verbose_name='slug')),
                ('tags', tagging.fields.TagField(max_length=255, verbose_name='tags', blank=True)),
                ('album', models.ForeignKey(to='porticus.Album')),
                ('related', models.ManyToManyField(related_name='related_rel_+', null=True, to='porticus.Ressource', blank=True)),
            ],
            options={
                'ordering': ('album', 'priority'),
                'verbose_name': 'ressource',
                'verbose_name_plural': 'ressources',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='ressource',
            unique_together=set([('album', 'slug')]),
        ),
        migrations.AddField(
            model_name='album',
            name='gallery',
            field=models.ForeignKey(to='porticus.Gallery'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='porticus.Album', null=True),
            preserve_default=True,
        ),
    ]
