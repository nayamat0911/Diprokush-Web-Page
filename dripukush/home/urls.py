from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('home/', views.basic, name='basic'),
    path('', views.home, name='home'),
]