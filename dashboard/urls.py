from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name= 'dashboard'),
    path('login/', views.login_view, name='login_view'),
     path('data/', views.data_view, name='data_view'),
]