from django.contrib import admin
from django.urls import path, include
from Project import views

urlpatterns = [
path('test', views.Project, name='Project'),
path('home', views.home, name='home'),
path('login', views.login_view,name='login'),
path('charts', views.chart,name='charts'),
path('table',views.contact,name='table'),
path('turbidity',views.turbidity,name='turbidity'),
path('location',views.location,name='location')
]