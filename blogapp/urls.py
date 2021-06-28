from django.contrib import admin
from django.urls import path 
from blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , views.index , name='home'),

    path("readmore/<id>/" , views.readmore , name='readmore'),

    path("blog" , views.blog , name='blog'),
    path("register" , views.register , name='register'),
    path("login" , views.login , name='login'),
    path("logout" , views.logout , name='logout'),
]
