from django.urls import path
from . import views
app_name='members_app'
urlpatterns = [

    path('', views.member_page, name='member_page'),
    path('member-form/', views.member_form, name='member_form'),
    path('member-list/', views.members_list, name='members_list'),
    path('member-info/<int:member_id>/', views.members_info, name='members_info'),
]