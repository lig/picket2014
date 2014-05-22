from django.conf.urls import patterns, include, url

from users.views import UserView


urlpatterns = patterns('',
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^profile/', include(UserView.urls)),
)
