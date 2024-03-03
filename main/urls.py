from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about_us/', views.about, name='about_us'),
    path('prices/', views.price, name='prices'),
    path('services/', views.service, name='services')
]