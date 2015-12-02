# coding: utf-8
from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.BlogHomeView.as_view(), name='blog_home'),
    url(r'^categoria/(?P<category_slug>[-\w]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^archivos/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^feed/$', views.LatestEntriesFeed()),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]*)/$', views.PostDetailView.as_view(), name='view_post'),

]
