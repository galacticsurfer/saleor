from django.conf.urls import url
from django.views.generic import RedirectView

from . import views


urlpatterns = [
    url(r'^onedream/$', RedirectView.as_view(url='https://goo.gl/forms/ClAVIeK1eDfhqGq92')),
    url(r'^$', views.home, name='home')

]
