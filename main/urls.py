from django.urls import path
from . import views

urlpatterns = [
path('home/', views.home, name='home'),
path('about/', views.about, name='about'),
path('contact/', views.ContactView.as_view(), name='contact'),
path('service/', views.ServiceView.as_view(), name='service'),
]

