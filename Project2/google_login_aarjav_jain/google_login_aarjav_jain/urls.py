from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from login.views import home
from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^$',  home, name='home'),
]
