"""car_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brands/', views.brands, name='brands'),
    path('brands/all_cars/', views.car_list_all, name='car-list-all'),
    # path('brands/new/', views.add_brand, name='add-brand'),
    # path('brands/<:id>/', views.brand_detail, name='brand-detail'),
    # path('brands/<:id>/edit/', views.edit_brand, name='edit-brand'),
    # path('brands/<:brand_id>/cars/', views.car_list, name='car-list'),
    # path('brands/<:brand_id>/cars/new', views.add_car, name='add-car'),
    # path('brands/<:brand_id>/cars/<:car_id>', views.car_detail, name='car-detail'),
    # path('brands/<:brand_id>/cars/<:car_id>/edit', views.edit_car, name='edit-car'),
]
