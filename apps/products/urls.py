from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^new_product/$', views.new_product, name="new_product"),
	url(r'^details/(?P<product_id>\d+)/$', views.details, name="details"),
	url(r'update/(?P<product_id>\d+)/$', views.update, name="update"),
	url(r'^delete/(?P<product_id>\d+)/$', views.delete, name="delete"),
]