# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Instagram'
        db.create_table('instagram_instagram', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('access_token', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('instagram', ['Instagram'])


    def backwards(self, orm):
        # Deleting model 'Instagram'
        db.delete_table('instagram_instagram')


    models = {
        'instagram.instagram': {
            'Meta': {'object_name': 'Instagram'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['instagram']