from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^user$', views.user, name='user'),
    url(r'^authenticate$', views.login, name='login'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^todo$', views.todo, name='todo'),
 	url(r'^bio$', views.bio, name='bio'),      
 	url(r'^bio/(?P<username>\w{0,50})$', views.bio_others,name='bio_other'),
 	url(r'^sanitize$', views.sanitize, name='sanitize'),  
 	url(r'^xtodo$', views.getXmenTodo, name='getXmenTodo'), 
    url(r'^xmenendpoint$', views.xmenendpoint, name='xmenendpoint'), 
 	url(r'^redirect$', views.redirect, name='redirect'), 
 	url(r'^hook$', views.hook, name='hook'),       
]
