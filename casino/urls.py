from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'check', views.check),
    url(r'login', views.login),
]
