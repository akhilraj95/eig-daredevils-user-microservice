from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^user$', views.user, name='user'),
    url(r'^authenticate$', views.login, name='login'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^todo$', views.todo, name='todo'),
 	url(r'^bio$', views.bio, name='bio'), 
 	url(r'^sanitize$', views.sanitize, name='sanitize'),  
 	url(r'^bio/(?P<username>\w{0,50})/$', views.bio_others,name='bio_other'),    
 	url(r'^avengerendpoint$', views.avengerendpoint, name='avengerendpoint'), 
 	url(r'^xtodo$', views.getAvengerTodo, name='getAvengerTodo'), 
]
