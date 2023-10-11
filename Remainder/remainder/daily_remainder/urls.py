from django.contrib import admin
from django.urls import path,include
# from django.contrib.auth import views
from . import views
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home, name='home'),
    # path('sign/', views.sign, name='sign'),
    # path('login/', views.login, name='login'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('',home),
    path('set-reminder/', views.set_reminder, name='set-reminder'),
    path('modify-reminder/', views.modify_reminder, name='modify-reminder'),
    path('disable-reminder/', views.disable_reminder, name='disable-reminder'),
    path('delete-reminder/', views.delete_reminder, name='delete-reminder'),
    path('enable-reminder/', views.enable_reminder, name='enable-reminder'),
    path('view-reminders/', views.view_reminders, name='view-reminders'),


    
]