from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shope_home'),
    path('about/', views.about, name='shope_about'),
]