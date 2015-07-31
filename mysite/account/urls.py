from django.conf.urls import patterns, include, url
from mysite.account.views.account_views import AddUserView
__author__ = 'Ahmad Abbad'

urlpatterns = patterns('',
                       url(r'/login', AddUserView.as_view()),
)

