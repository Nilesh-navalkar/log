from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.route,name='route'),
    path('patient', views.logp,name='logp'),
    path('docter', views.logd,name='logd'),
    path('signup', views.register,name='register'),
    path('logout', views.log_out,name='logout'),
    path('home', views.home,name='home'),
]
