from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('cars/<int:pk>/', views.car_detail, name="car_detail"),
    path('driverform/',views.driver_form,name="driver_form"),
    path('carform/',views.car_form,name="car_form"),
    path('cars/',views.driver_detail,name="driver_detail"),
]