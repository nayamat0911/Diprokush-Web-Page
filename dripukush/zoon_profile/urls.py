from django.urls import path
from . import views
app_name='zoon_profile'
urlpatterns = [
    path('zoon1/', views.Chittagong, name='chittagong_page'),
    path('zoon2/', views.Cumilla, name='cumilla_page'),
    path('zoon3/', views.Syllet, name='syllet_page'),
    # path('home/', views.home, name='home'),
]
