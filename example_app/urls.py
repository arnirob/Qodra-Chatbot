from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from example_app.views import ChatterBotAppView, ChatterBotApiView,DocumentoinFileView
from example_app import views


urlpatterns = [
    url(r'^$', ChatterBotAppView.as_view(), name='main'),
    url(r'^admin/', admin.site.urls, name='admin'),    
    url(r'^api/chatterbot/',views.test, name='chatterbot'),    
	url(r'^api/doc', DocumentoinFileView.as_view(), name='docs'),

	# url(r'^api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
	# path('/api/chatterbot',views.test, name='chatterbot'),    
]
