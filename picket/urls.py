from django.conf.urls import patterns, include, url

from .views import IssueView


urlpatterns = patterns('',
    url(r'^', include(IssueView.urls)),
    url(r'^accounts/', include('users.urls')),
)
