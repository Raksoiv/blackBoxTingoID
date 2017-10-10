from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'detalle', views.detalle),
    url(r'login', views.login),
    url(r'discount', views.discount),
]
