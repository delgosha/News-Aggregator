from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.articles_list, name = 'articles_list'),
	url(r'^feeds/$', views.feeds_list, name = 'feeds_list'),
	url(r'^feeds/add/$', views.add_feed, name = 'add_feed')
]