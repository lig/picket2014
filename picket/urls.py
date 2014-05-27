from django.conf.urls import patterns, include, url

from .views import ProjectView, IssueView


urlpatterns = patterns('',
    url(r'^', include(ProjectView.urls)),
    url(r'^', include(IssueView.urls)),
    url(r'^accounts/', include('users.urls')),
)
