from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^', views.shorten),
	url(r'^submit/', views.shorten),
]
