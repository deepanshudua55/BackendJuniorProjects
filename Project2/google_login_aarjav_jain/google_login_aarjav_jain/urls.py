from django.contrib import admin
from django.urls import path
from login import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login, name='login'),
    #url(r'^logout/$', views.logout, name='logout'),
    #url(r'^auth/', include('login.urls', namespace='login')),
    url(r'^$', views.home, name='home'),
]
