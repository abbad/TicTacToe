__author__ = 'Ahmad Abbad'

from django.db import models


class Account(models.Model):
    # Personal information
    username = models.CharField(max_length=128,  null=True)


    # TODO: move these fields to tictactoe app and make a one to one relation with account app.
    wins = models.IntegerField(null=False, blank=False, default=0)
    losses = models.IntegerField(null=True, blank=False, default=0)
    draws = models.IntegerField(null=True, blank=False, default=0)