from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^kotel', views.kotel, name='kotel'),
    url(r'^$', views.post_list, name='post_list'),
	
]