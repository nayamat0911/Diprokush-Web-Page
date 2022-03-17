from django.urls import path
from . import views
app_name='commitee_app'
urlpatterns = [
    path('', views.commitee, name='commitee'),
    # path('', views.home, name='home'),
]