from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView


urlpatterns = [

    path('', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('signup/', views.user_signup, name='user_signup'),
    path('userProfile/', views.userProfile, name='userProfile'),
    path('changed_password/', views.changed_password, name='changed_password'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    # path('home/', views.home, name='home'),

    path('reset/password/', PasswordResetView.as_view(template_name='session/reset_passowr.html'), name='password_reset'),
    path('reset/password/done/', PasswordResetDoneView.as_view(template_name='session/reset_password_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='session/reset_password_confrim.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetView.as_view(template_name='session/password_reset_complete.html'), name='password_reset_complete'),
]