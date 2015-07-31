from django.conf.urls import patterns, include, url
#from mysite.tictactoe.views.game import HomeView
__author__ = 'Ahmad Abbad'


urlpatterns = patterns('',
    url(r'^', include('mysite.tictactoe.urls', namespace = 'tictactoe', app_name='tictactoe')),
    url(r'^account$', include('mysite.account.urls', namespace ='account', app_name='account')),
)