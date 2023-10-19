from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register("transactions", views.TransactionViewSet,basename='transactions')
urlpatterns = [
      path("api/", include(router.urls)),
    path('', views.dashboard, name= 'dashboard'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('login/', views.login, name='login'),
     path('data/', views.data_view, name='data_view'),
]