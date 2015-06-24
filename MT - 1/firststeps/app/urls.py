from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^', views.process_form),
	url(r'^submit/', views.process_form),
]
