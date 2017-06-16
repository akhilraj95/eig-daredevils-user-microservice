from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^user$', views.user, name='user'),
    url(r'^authenticate$', views.login, name='login'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
]
