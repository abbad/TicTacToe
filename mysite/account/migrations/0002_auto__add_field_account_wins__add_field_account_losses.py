# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Account.wins'
        db.add_column(u'account_account', 'wins',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Account.losses'
        db.add_column(u'account_account', 'losses',
                      self.gf('django.db.models.fields.IntegerField')(default=0, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Account.wins'
        db.delete_column(u'account_account', 'wins')

        # Deleting field 'Account.losses'
        db.delete_column(u'account_account', 'losses')


    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'losses': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'wins': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['account']