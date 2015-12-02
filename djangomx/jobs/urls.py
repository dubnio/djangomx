# coding: utf-8
from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^$', views.JobsHomeView.as_view(), name='jobs_home'),
    url(r'^nueva$', views.new_job, name='new_job'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]*)/$',
        views.JobDetailView.as_view(), name='job_detail'),

]
