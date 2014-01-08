# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Blog.teaser'
        db.add_column(u'blog_blog', 'teaser',
                      self.gf('django.db.models.fields.TextField')(default='a'),
                      keep_default=False)


        # Changing field 'Blog.title'
        db.alter_column(u'blog_blog', 'title', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'BlogImage.title'
        db.alter_column(u'blog_blogimage', 'title', self.gf('django.db.models.fields.CharField')(max_length=256))

    def backwards(self, orm):
        # Deleting field 'Blog.teaser'
        db.delete_column(u'blog_blog', 'teaser')


        # Changing field 'Blog.title'
        db.alter_column(u'blog_blog', 'title', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'BlogImage.title'
        db.alter_column(u'blog_blogimage', 'title', self.gf('django.db.models.fields.CharField')(max_length=128))

    models = {
        u'blog.blog': {
            'Meta': {'object_name': 'Blog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tag.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'teaser': ('django.db.models.fields.TextField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'blog.blogimage': {
            'Meta': {'object_name': 'BlogImage'},
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Blog']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'tag.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['blog']