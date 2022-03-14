from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('', views.basic, name='basic'),
    path('home/', views.home, name='home'),
]