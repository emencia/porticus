# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field related on 'Ressource'
        m2m_table_name = db.shorten_name(u'porticus_ressource_related')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_ressource', models.ForeignKey(orm[u'porticus.ressource'], null=False)),
            ('to_ressource', models.ForeignKey(orm[u'porticus.ressource'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_ressource_id', 'to_ressource_id'])


    def backwards(self, orm):
        # Removing M2M table for field related on 'Ressource'
        db.delete_table(db.shorten_name(u'porticus_ressource_related'))


    models = {
        u'porticus.album': {
            'Meta': {'object_name': 'Album'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['porticus.Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['porticus.Album']"}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'template_name': ('django.db.models.fields.CharField', [], {'default': "'porticus/album_detail.html'", 'max_length': '255'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'porticus.gallery': {
            'Meta': {'ordering': "('-priority', 'name')", 'object_name': 'Gallery'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'template_name': ('django.db.models.fields.CharField', [], {'default': "'porticus/gallery_detail.html'", 'max_length': '255'})
        },
        u'porticus.ressource': {
            'Meta': {'ordering': "('-priority', 'name')", 'object_name': 'Ressource'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['porticus.Album']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'file': ('filebrowser.fields.FileBrowseField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'file_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'file_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'file_weight': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'related': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_rel_+'", 'null': 'True', 'to': u"orm['porticus.Ressource']"}),
            'tags': ('tagging.fields.TagField', [], {})
        }
    }

    complete_apps = ['porticus']