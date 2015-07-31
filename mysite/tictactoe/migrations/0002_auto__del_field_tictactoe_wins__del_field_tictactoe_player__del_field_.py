# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'TicTacToe.wins'
        db.delete_column(u'tictactoe_tictactoe', 'wins')

        # Deleting field 'TicTacToe.player'
        db.delete_column(u'tictactoe_tictactoe', 'player_id')

        # Deleting field 'TicTacToe.losses'
        db.delete_column(u'tictactoe_tictactoe', 'losses')


    def backwards(self, orm):
        # Adding field 'TicTacToe.wins'
        db.add_column(u'tictactoe_tictactoe', 'wins',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TicTacToe.player'
        db.add_column(u'tictactoe_tictactoe', 'player',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['account.Account'], unique=True, null=True),
                      keep_default=False)

        # Adding field 'TicTacToe.losses'
        db.add_column(u'tictactoe_tictactoe', 'losses',
                      self.gf('django.db.models.fields.IntegerField')(default=0, null=True),
                      keep_default=False)


    models = {
        u'tictactoe.tictactoe': {
            'Meta': {'object_name': 'TicTacToe'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['tictactoe']