from django.conf.urls import patterns, include, url
from mysite.tictactoe.views.game import HomeView, AddLossView, AddWinView, StartGame, AddDraw
__author__ = 'Ahmad Abbad'

urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view(), name='index'),
                       url(r'^add_loss', AddLossView.as_view(), name='add_loss'),
                       url(r'^add_win', AddWinView.as_view(), name='add_win'),
                       url(r'^add_draw', AddDraw.as_view(), name='add_draw'),
                       url(r'tictactoe/play$', StartGame.as_view(), name='start_game'),
)
