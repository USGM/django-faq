# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Question.updated_by'
        db.delete_column(u'faq_question', 'updated_by_id')

        # Deleting field 'Question.created_on'
        db.delete_column(u'faq_question', 'created_on')

        # Deleting field 'Question.created_by'
        db.delete_column(u'faq_question', 'created_by_id')

        # Deleting field 'Question.updated_on'
        db.delete_column(u'faq_question', 'updated_on')


    def backwards(self, orm):
        # Adding field 'Question.updated_by'
        db.add_column(u'faq_question', 'updated_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['membership.User']),
                      keep_default=False)

        # Adding field 'Question.created_on'
        db.add_column(u'faq_question', 'created_on',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Question.created_by'
        db.add_column(u'faq_question', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['membership.User']),
                      keep_default=False)

        # Adding field 'Question.updated_on'
        db.add_column(u'faq_question', 'updated_on',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 8, 22, 0, 0)),
                      keep_default=False)


    models = {
        u'faq.question': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Question'},
            'answer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'protected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': u"orm['faq.Topic']"})
        },
        u'faq.topic': {
            'Meta': {'ordering': "['sort_order', 'name']", 'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['faq']