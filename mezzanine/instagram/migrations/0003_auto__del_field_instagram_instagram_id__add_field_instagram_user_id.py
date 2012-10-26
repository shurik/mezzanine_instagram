# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Instagram.instagram_id'
        db.delete_column('instagram_instagram', 'instagram_id')

        # Adding field 'Instagram.user_id'
        db.add_column('instagram_instagram', 'user_id',
                      self.gf('django.db.models.fields.IntegerField')(default=122844),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Instagram.instagram_id'
        db.add_column('instagram_instagram', 'instagram_id',
                      self.gf('django.db.models.fields.IntegerField')(default=122844),
                      keep_default=False)

        # Deleting field 'Instagram.user_id'
        db.delete_column('instagram_instagram', 'user_id')


    models = {
        'instagram.instagram': {
            'Meta': {'object_name': 'Instagram'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['instagram']