# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project.description'
        db.delete_column(u'project_project', 'description')

        # Deleting field 'Project.brief_description'
        db.delete_column(u'project_project', 'brief_description')

        # Adding field 'Project.teaser'
        db.add_column(u'project_project', 'teaser',
                      self.gf('django.db.models.fields.TextField')(default='a'),
                      keep_default=False)

        # Adding field 'Project.text'
        db.add_column(u'project_project', 'text',
                      self.gf('django.db.models.fields.TextField')(default='a'),
                      keep_default=False)


        # Changing field 'Project.title'
        db.alter_column(u'project_project', 'title', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'Project.url'
        db.alter_column(u'project_project', 'url', self.gf('django.db.models.fields.SlugField')(max_length=256))

        # Changing field 'ProjectLog.title'
        db.alter_column(u'project_projectlog', 'title', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'ShowcaseImage.title'
        db.alter_column(u'project_showcaseimage', 'title', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'ShowcaseCode.title'
        db.alter_column(u'project_showcasecode', 'title', self.gf('django.db.models.fields.CharField')(max_length=256))

    def backwards(self, orm):
        # Adding field 'Project.description'
        db.add_column(u'project_project', 'description',
                      self.gf('django.db.models.fields.TextField')(default='a'),
                      keep_default=False)

        # Adding field 'Project.brief_description'
        db.add_column(u'project_project', 'brief_description',
                      self.gf('django.db.models.fields.TextField')(default='a'),
                      keep_default=False)

        # Deleting field 'Project.teaser'
        db.delete_column(u'project_project', 'teaser')

        # Deleting field 'Project.text'
        db.delete_column(u'project_project', 'text')


        # Changing field 'Project.title'
        db.alter_column(u'project_project', 'title', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Project.url'
        db.alter_column(u'project_project', 'url', self.gf('django.db.models.fields.SlugField')(max_length=128))

        # Changing field 'ProjectLog.title'
        db.alter_column(u'project_projectlog', 'title', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'ShowcaseImage.title'
        db.alter_column(u'project_showcaseimage', 'title', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'ShowcaseCode.title'
        db.alter_column(u'project_showcasecode', 'title', self.gf('django.db.models.fields.CharField')(max_length=128))

    models = {
        u'project.project': {
            'Meta': {'object_name': 'Project'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tag.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'teaser': ('django.db.models.fields.TextField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '256'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        u'project.projectlog': {
            'Meta': {'object_name': 'ProjectLog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'project.showcasecode': {
            'Meta': {'object_name': 'ShowcaseCode'},
            'code': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'project.showcaseimage': {
            'Meta': {'object_name': 'ShowcaseImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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

    complete_apps = ['project']