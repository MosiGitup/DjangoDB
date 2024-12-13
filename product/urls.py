from django.urls import path
from . import views

urlpatterns = [
    path('users/DBhome/', views.DBhome, name='DBhome'),
    path('users/DBhome/<slug:project_slug>/', views.DBhome, name='DBhome_by_project'),
    path('catalog/', views.region_list, name='region_list'),
    path('catalog/<slug:project_slug>/', views.region_list, name='list_by_project'),
    path('catalog/region/<int:id>/<slug:slug>/', views.region_detail, name='region_detail'),
    path('catalog/region/<slug:region>/<slug:slug>/<int:id>/', views.product_detail, name='product_detail'),
    # path('DBhome/product/', views.product_catalog, name='product_catalog'),
    # path('DBhome/product/<slug:project_slug>/', views.product_catalog, name='product_catalog_by_project'),
    path('product/', views.secondHome, name='secondHome'),
]
