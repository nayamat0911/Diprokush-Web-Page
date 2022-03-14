from django.urls import path
from . import views
app_name='about_app'
urlpatterns = [

    path('', views.about_page, name='about_page'),
    # path('home/', views.home, name='home'),
]