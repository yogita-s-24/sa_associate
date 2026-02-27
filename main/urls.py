from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('services/', views.services, name='services'),
    path('certificates/', views.certificates, name='certificates'),
    path('awards/', views.awards, name='awards'),
    path('contact/', views.contact, name='contact'),
]
