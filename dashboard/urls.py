from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register("transactions", views.TransactionViewSet,basename='transactions')
urlpatterns = [
      path("api/", include(router.urls)),
    path('', views.dashboard, name= 'dashboard'),
  
     path('data/', views.data_view, name='data_view'),
]