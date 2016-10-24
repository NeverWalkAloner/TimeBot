from django.conf.urls import url
from .views import TimeView
from django.conf import settings


urlpatterns = [
    url(r'^{}/$'.format(settings.TGRM_TOKEN[-35:]), TimeView.as_view(), name='main'),
]
