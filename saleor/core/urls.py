from django.conf.urls import url
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^fairplay/$', RedirectView.as_view(url='https://goo.gl/forms/ETpuzSnOxvw1EtZ72')),
]
