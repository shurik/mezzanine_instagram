# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Instagram.instagram_id'
        db.add_column('instagram_instagram', 'instagram_id',
                      self.gf('django.db.models.fields.IntegerField')(default=122844),
                      keep_default=False)

        # Adding field 'Instagram.username'
        db.add_column('instagram_instagram', 'username',
                      self.gf('django.db.models.fields.CharField')(default='shurik', max_length=255),
                      keep_default=False)

        # Adding field 'Instagram.full_name'
        db.add_column('instagram_instagram', 'full_name',
                      self.gf('django.db.models.fields.CharField')(default='Aleksandr Vladimirskiy', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Instagram.instagram_id'
        db.delete_column('instagram_instagram', 'instagram_id')

        # Deleting field 'Instagram.username'
        db.delete_column('instagram_instagram', 'username')

        # Deleting field 'Instagram.full_name'
        db.delete_column('instagram_instagram', 'full_name')


    models = {
        'instagram.instagram': {
            'Meta': {'object_name': 'Instagram'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instagram_id': ('django.db.models.fields.IntegerField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['instagram']