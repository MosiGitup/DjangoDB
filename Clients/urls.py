from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login_page'),
    path('users/register/', views.register_page, name='register_page'),
    path('users/logout', views.logout_page, name='logout_page'),
    path('users/contact', views.contact, name='s_contact'),
    path('users/forget_pass', views.forget_pass, name='forget_pass'),
]
