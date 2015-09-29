from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^review', views.reviews_list, name='reviews_list'),
    #url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^add$', views.post_new, name='post_new'),
    url(r'^$', views.get_url, name='get_url'),
]