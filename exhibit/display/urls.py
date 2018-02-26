from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^home/$', views.home, name='home'),
    url(r'^search/$', views.search_reults, name='search_results')
]
