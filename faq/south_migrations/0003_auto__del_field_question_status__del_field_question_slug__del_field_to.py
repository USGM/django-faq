# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Question.status'
        db.delete_column(u'faq_question', 'status')

        # Deleting field 'Question.slug'
        db.delete_column(u'faq_question', 'slug')

        # Deleting field 'Topic.slug'
        db.delete_column(u'faq_topic', 'slug')


    def backwards(self, orm):
        # Adding field 'Question.status'
        db.add_column(u'faq_question', 'status',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Question.slug'
        db.add_column(u'faq_question', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='old_question', max_length=100),
                      keep_default=False)

        # Adding field 'Topic.slug'
        db.add_column(u'faq_topic', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='old_topic', max_length=150),
                      keep_default=False)


    models = {
        u'faq.question': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Question'},
            'answer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'protected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': u"orm['faq.Topic']"})
        },
        u'faq.topic': {
            'Meta': {'ordering': "['sort_order', 'name']", 'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['faq']