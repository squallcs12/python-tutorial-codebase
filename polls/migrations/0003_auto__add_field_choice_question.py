# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Choice.question'
        db.add_column(u'polls_choice', 'question',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='choices', to=orm['polls.Question']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Choice.question'
        db.delete_column(u'polls_choice', 'question_id')


    models = {
        'polls.choice': {
            'Meta': {'object_name': 'Choice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'choices'", 'to': "orm['polls.Question']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'polls.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['polls']