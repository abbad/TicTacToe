# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TicTacToe'
        db.create_table(u'tictactoe_tictactoe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['account.Account'], unique=True, null=True)),
            ('wins', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('losses', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
        ))
        db.send_create_signal(u'tictactoe', ['TicTacToe'])


    def backwards(self, orm):
        # Deleting model 'TicTacToe'
        db.delete_table(u'tictactoe_tictactoe')


    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'})
        },
        u'tictactoe.tictactoe': {
            'Meta': {'object_name': 'TicTacToe'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'losses': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'player': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['account.Account']", 'unique': 'True', 'null': 'True'}),
            'wins': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['tictactoe']