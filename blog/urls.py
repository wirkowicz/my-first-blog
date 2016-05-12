from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^kotel', views.kotel, name='kotel'),
    url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	# zmienna pk jest przesylana do widoku post detail
]