from django.conf.urls import patterns, url, include

from .views import IssueView


urlpatterns = patterns('',
    url(r'^$', include(IssueView.urls)),
)
